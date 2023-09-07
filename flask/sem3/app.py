from flask import Flask, request, make_response, render_template, session, redirect, url_for, flash
from models import db, User
from flask_wtf import FlaskForm
from ignorefile import s_key   # добавлен в gitignore
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.csrf import CSRFProtect
import time
import bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = s_key
app.secret_key  = s_key
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Database created')

@app.route('/')
def index():
    if 'email' in session:
        return redirect(url_for('greating'))
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    context = {'title': 'Вход'}
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        check = request.form.get('password').encode('utf-8')
        users = User.query.filter(User.email == request.form.get('email')).all()
        if users and bcrypt.checkpw(check, users[0].password):
            session['email'] = request.form.get('email') or 'NoEmail'
            session['username'] = users[0].username
            return redirect(url_for('greating'))
        flash('Неверный логин или пароль!', 'warning')
        return redirect(url_for('login'))
    return render_template('login_form.html', form=form, **context)

@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    context = {'title': 'Регистрация'}
    if 'email' in session:
        return redirect(url_for('logined'))
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        try:
            password = request.form.get('password').encode('utf-8')
            hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
            user = User(username = request.form.get('username'),
                        email = request.form.get('email'),
                        password = hashed)
            db.session.add(user)
            db.session.commit()
            flash(f'''Пользователь зарегистрирован! Войдите что бы продолжить''', 'success')
            return redirect(url_for('login'))
        except:
            flash(f'''Такой пользователь уже существует''', 'success')
            return redirect(url_for('registration'))
    return render_template('registration_form.html', form = form, **context)


@app.route('/greating/')
def greating():
    context = {'title': 'Приветствие', 'username': session['username']}
    return render_template('main.html', **context)

@app.route('/logined/')
def logined():
    context = {'title': 'Предупреждение', 'username': session['username']}
    return render_template('logined.html', **context)

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)

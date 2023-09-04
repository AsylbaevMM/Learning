from flask import Flask, request, make_response, render_template, session, redirect, url_for


app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def index():
    if 'username' in session:
        redirect(url_for('greating'))
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    context = {'title': 'Авторизация' }
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        session['email'] = request.form.get('email') or 'NoEmail'
        return redirect(url_for('greating'))
    return render_template('login_form.html')

@app.route('/greating/')
def greating():
    context = {'title': 'Приветсвие', 'username': session['username'], 'email': session['email']}
    return render_template('greating.html', **context)


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index'))

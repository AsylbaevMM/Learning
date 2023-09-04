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
        response = make_response(redirect(url_for('greating')))
        name = request.form.get('username') or 'NoName'
        response.set_cookie('username', str(name))
        email = request.form.get('email') or 'NoEmail'
        response.set_cookie('email', str(email))
        return response
    return render_template('login_form.html')

@app.route('/greating/')
def greating():
    context = {'title': 'Приветсвие', 'username': request.cookies.get('username'), 'email': request.cookies.get('email')}
    return render_template('greating.html', **context)


@app.route('/logout/')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('email', 'None', max_age = 0)
    response.set_cookie('username', 'None', max_age=0)
    return response

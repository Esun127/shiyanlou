#!/usr/bin/env python3

from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'Esun127 is god body'

@app.route('/')
def index():
    if 'username' in session:
        return 'Welcome {} back'.format(session.get('username'))
    else:
        return redirect(url_for('login'))

def valid_login(user, passwd):
    if user == 'admin' and passwd == '123456':
        return True
    return False


def log_the_user_in(user):
    msg = 'welcom {} back'.format(user)
#    print(msg)
#    return redirect(url_for('login.html', error=msg))
    return msg

@app.route('/failue')
def login_failed():
    error = 'Invalid username or password'
    return error



@app.route('/login', methods=['POST','GET'])
def login():
    error =  None
    print(request.method)
    if request.method == "POST":
        print('---------------------------POST')
        if valid_login(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            error = log_the_user_in(request.form['username'])
        else:
            #error = 'Invalid username or password'
            return redirect(url_for('login_failed'))

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)

    with app.test_request_context('/hello', method='POST'):
        assert request.path == '/hello'
        assert request.method == 'POST'





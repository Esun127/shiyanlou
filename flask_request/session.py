#!/usr/bin/env python3
from flask import Flask, render_template, session, redirect, url_for, request, escape
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logined in as {}'.format(escape(session['username']))
    return 'You are not logged in'

@app.route('/login', methods=['POST',"GET"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action='' method='POST'>
            <input type='text' name='username'><br>
            <input type='submit' value='Login'><br>
        </form>
        '''


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python3
from flask import request, Flask, render_template, make_response

app = Flask(__name__)

@app.route('/hello')
def get_username_from_cookies():
    username = request.cookies.get('username')
    return 'Hello '+username


@app.route('/put/<username>')
def put_username_to_cookies(username):
    resp = make_response('put {} to cookies ok'.format(username))
    resp.set_cookie('username', username)
    return resp


if __name__ == '__main__':
    app.run(debug=True)

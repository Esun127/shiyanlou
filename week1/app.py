#!/usr/bin/env python3
from flask import Flask, render_template, url_for, redirect, request, make_response
import flask
app = Flask(__name__)


# flask pei zhi guan li
app.config.update({
				'SECRET_KEY': 'a random string' # pei zhi yi ge mi yao
				})

#ap.config.from_pyfile('</path/to/config.py>')  # sheng can huan jing zhong 


												# geng xin pei zhi wen jian 
@app.route('/')
def index():
#	return 'Hello World!'
	username = request.cookies.get('username')
#	return redirect(url_for('user_index', username=username))
	return 'Hello {}!.'.format(username)

@app.route('/user/<username>')
def user_index(username):
#	return "Hello {}".format(username)
	print(app.config['SECRET_KEY'])
	print(request.headers.get('User-Agent'))
	if username == 'invalid':
		flask.abort(404)
	resp = make_response(render_template('user_index.html', username=username))
#	return render_template('user_index.html', username=username)
	resp.set_cookie('username', username)
	return resp

@app.route('/post/<int:post_id>')
def show_post(post_id):
	print(request.method, request.args.get('name'))
	return 'Post {}'.format(post_id)


@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404



if __name__ == '__main__':
	app.run(host='0.0.0.0')
	#except Exception as e:
#	with app.request_context(envrion):
		
#	print(request.method())

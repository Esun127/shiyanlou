#!/usr/bin/env python3


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello Shiyanlou!'

@app.route('/courses/<name>')
def get_courses(name):
	#return 'Courses:{}'.format(name)
	return render_template('courses.html', name=name)

if __name__ == '__main__':
	app.run()

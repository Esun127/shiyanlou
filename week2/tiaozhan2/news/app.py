#!/usr/bin/env python3


from flask import Flask, render_template, abort
import os
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/news'

db = SQLAlchemy(app)

class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    created_time= db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category', backref=db.backref('files'))

    def __repr__(self):
        return 'File(title={})'.format(self.title)
    
    def __init__(self, title, created_time, category, content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content



class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return 'Category(name={})'.format(self.name)

    def __init__(self, name):
        self.name = name




@app.route('/')
def index():
    res = []
    #path=os.path.abspath('.')
    #os.chdir('..')
    #path  = os.getcwd()
 #   os.chdir('/home/shiyanlou/files')
    files = File.query.all()
    for i in files:
        res.append((i.id, i.title))

    return render_template('index.html',data=res)

@app.route('/files/<file_id>')
def get_file(file_id):
    content = []
    res =  File.query.filter_by(id=file_id).first()
    if res:
        category = Category.query.filter_by(id=res.category_id).first()
        if not res:
            abort(404)
        content.append((res.content, res.created_time, category.name))
        return render_template('file.html', data=content)
    else:
        #retun redirect(url_for('404.html'))
        abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)

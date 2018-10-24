#!/usr/bin/env python3


from flask import Flask, render_template, abort
import os
import json

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    titles = []
    #path=os.path.abspath('.')
    #os.chdir('..')
    #path  = os.getcwd()
 #   os.chdir('/home/shiyanlou/files')
    path = '/home/shiyanlou/files'
    os.chdir(path)
    for i in os.listdir():
        abspath =  path + '/' + i
        print(abspath)
        if os.path.isfile(abspath):
            with open(abspath) as f:
                dt = json.loads(f.read())
                titles.append(dt['title'])

    return render_template('index.html',titles=titles)

@app.route('/files/<filename>')
def get_file(filename):
    content = None
   # os.chdir('../files')
    path = '/home/shiyanlou/files'
    abspath = path + '/' + filename + '.json'
    if os.path.exists(abspath):
        with open(abspath) as f:
            content = json.loads(f.read())
            return render_template('file.html', content=content)
    else:
        #retun redirect(url_for('404.html'))
        abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)

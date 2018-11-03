#!/usr/bin/env python3

from flask import request, Flask
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['POST',"GET"])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/tmp/upload_file.txt' + secure_filename(f.filename))

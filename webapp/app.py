from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from logger import logger
import os.path

import logging


UPLOAD_FOLDER = '/var/lib/khal-remove/uploads'
app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

for handler in logging.getLogger('gunicorn.error').handlers:
    app.logger.addHandler(handler)

@app.route('/')
def index():
    return send_file('static/index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return ""

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9999, debug=True)

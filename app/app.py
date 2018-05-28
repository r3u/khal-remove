# KHAL | REMOVE | 2.0
# Copyright (C) 2018  Rachael Melanson
# Copyright (C) 2018  Henry Rodrick
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from flask import Flask, flash, request, redirect
from flask import url_for, send_file, abort, jsonify
from werkzeug.utils import secure_filename
from logger import logger
import os.path

import logging
import tasks


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
        return jsonify({
            "error": "Missing file"
        }), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({
            "error": "Missing file"
        }), 400
    filename = secure_filename(file.filename)
    abs_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(abs_path)
    res = tasks.process.delay(abs_path)
    return jsonify({
        "jobId": res.id
    })

@app.route('/job/<jobid>', methods=['GET'])
def get_job_status(jobid):
    return jsonify(tasks.state(jobid))

@app.route('/result/<jobid>', methods=['GET'])
def get_result(jobid):
    res = tasks.get(jobid)
    if res:
        return res
    else:
        return abort(404)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9999, debug=True)

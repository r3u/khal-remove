import flask
from logger import logger

import logging

application = flask.Flask(__name__, static_url_path='')

for handler in logging.getLogger('gunicorn.error').handlers:
    application.logger.addHandler(handler)

@application.route('/')
def index():
    return flask.send_file('static/index.html')

@application.route('/api/v1/hello')
def hello():
    return "Hello"

if __name__ == "__main__":
    application.run(host='127.0.0.1', port=9999, debug=True)

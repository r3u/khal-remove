from flask import Flask
from logger import logger

import logging

application = Flask(__name__)

for handler in logging.getLogger('gunicorn.error').handlers:
    application.logger.addHandler(handler)

@application.route("/")
def index():
    logger.info("Loading index")
    return "<h1 style='color:#333333; font-family: monospace;'>Oh hello!</h1>"

if __name__ == "__main__":
    application.run(host='127.0.0.1', port=9999, debug=True)

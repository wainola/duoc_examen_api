import flask
import os
from flask import request, jsonify, redirect, url_for
from dotenv import load_dotenv
from flask_dance.contrib.google import make_google_blueprint, google
from flask_cors import CORS

from handlers.loginHandler import login
from handlers.userHandler import user
from handlers.creditHandler import credit
from handlers.executiveHandler import executive
from handlers.requestStatusHandler import request_status
from handlers.signupHandler import signup

load_dotenv()

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.secret_key='supersecretkey'
CORS(app)

app.register_blueprint(login, url_prefix='/api')
app.register_blueprint(user, url_prefix='/api')
app.register_blueprint(credit, url_prefix='/credit')
app.register_blueprint(executive, url_prefix='/api')
app.register_blueprint(request_status, url_prefix='/request_status')
app.register_blueprint(signup, url_prefix='/api')


if __name__ == '__main__':
  app.run()
import flask
import os
from flask import request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS

from handlers.loginHandler import login
from handlers.userHandler import user
from handlers.creditHandler import credit
from handlers.executiveHandler import executive
from handlers.requestStatusHandler import request_status
from handlers.signupHandler import signup
from handlers.testHandler import testBlueprint

load_dotenv()

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.secret_key='supersecretkey'
CORS(app)

app.register_blueprint(login, url_prefix='/api')
app.register_blueprint(user, url_prefix='/api')
app.register_blueprint(credit, url_prefix='/credit')
app.register_blueprint(executive, url_prefix='/api')
app.register_blueprint(request_status, url_prefix='/api')
app.register_blueprint(signup, url_prefix='/api')
app.register_blueprint(testBlueprint, url_prefix='/api')

if __name__ == '__main__':
  app.run()
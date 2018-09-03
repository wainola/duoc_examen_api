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

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
REDIRECT_URL = '/oauth2callback'

blueprint = make_google_blueprint(
  client_id=GOOGLE_CLIENT_ID,
  client_secret=GOOGLE_CLIENT_SECRET,
  scope=[
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
    ],
    redirect_url='http://localhost:3001'
)

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.secret_key='supersecretkey'
CORS(app)

app.register_blueprint(blueprint, url_prefix='/login')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(credit, url_prefix='/credit')
app.register_blueprint(executive, url_prefix='/executive')
app.register_blueprint(request_status, url_prefix='/request_status')
app.register_blueprint(signup, url_prefix='/signup')


@app.route("/")
def index():
    if not google.authorized:
        # return jsonify({ 'msg': False})
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text

if __name__ == '__main__':
  app.run()
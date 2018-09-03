import flask
from flask import request, jsonify, redirect, url_for
from dotenv import load_dotenv
from flask_dance.contrib.google import make_google_blueprint, google
import os

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
    ]
)

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.secret_key='supersecretkey'

app.register_blueprint(blueprint, url_prefix='/login')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(credit, url_prefix='/credit')
app.register_blueprint(executive, url_prefix='/executive')
app.register_blueprint(request_status, url_prefix='/request_status')
app.register_blueprint(signup, url_prefix='/signup')


@app.route("/singin")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    print('resp::::::::::::::::::::::', resp)
    assert resp.ok, resp.text
    return "You are {email} on Google".format(email=resp.json()["email"])

if __name__ == '__main__':
  app.run()
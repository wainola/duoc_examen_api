from flask import jsonify, Blueprint

signup = Blueprint('signup', __name__)

@signup.route('/')
def get():
  return jsonify({ 'msng': 'get method signup'})
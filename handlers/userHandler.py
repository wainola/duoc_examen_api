from flask import jsonify, Blueprint

user = Blueprint('user', __name__)

@user.route('/')
def get():
  return jsonify({ 'msng': 'get method user'})
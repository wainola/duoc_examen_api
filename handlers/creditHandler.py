from flask import jsonify, Blueprint

credit = Blueprint('credit', __name__)

@credit.route('/')
def get():
  return jsonify({ 'msng': 'get method credit'})
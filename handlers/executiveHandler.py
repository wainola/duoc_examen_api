from flask import jsonify, Blueprint

executive = Blueprint('executive', __name__)

@executive.route('/')
def get():
  return jsonify({ 'msng': 'get method executive'})
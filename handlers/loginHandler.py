from flask import jsonify, Blueprint

login = Blueprint('login', __name__)

@login.route('/superlogin')
def hi():
  return jsonify({ 'msg': 'Hola desde modulo'})
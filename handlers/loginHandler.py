from flask import request, jsonify, Blueprint

login = Blueprint('login', __name__)

@login.route('', methods=['POST'])
def hi():
  print('dotenv', os.getenv('GOOGLE_CLIENT_ID'))
  print('request', request.method)
  return jsonify({ 'msg': 'Hola desde modulo'})

from flask import jsonify, Blueprint

request_status = Blueprint('request_status', __name__)

@request_status.route('/')
def getStatus():
  return jsonify({ 'msg': 'request status handler'})
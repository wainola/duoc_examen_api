from flask import jsonify, request, Blueprint

testBlueprint = Blueprint('testing', __name__)

@testBlueprint.route('/test', methods=['GET'])
def requestTest():
    if request.method == 'GET':
        return jsonify({ 'msg': 'testing', 'status': 200})
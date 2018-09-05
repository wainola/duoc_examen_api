import sqlite3
import os
from flask import jsonify, Blueprint, request

request_status = Blueprint('request_status', __name__)

current_directory = os.getcwd()
DB_PATH = f'{current_directory}/db/db_examen.db'

conn = sqlite3.connect(DB_PATH)

@request_status.route('/request_status', methods=['POST', 'GET'])
def estado_solicitud():
  if request.method == 'POST':
    estado_solicitud = request.get_json()['request_status']

    id = estado_solicitud['id']
    estado_sol = estado_solicitud['estado_solicitud']

    sql =  '''
            INSERT INTO estado_solicitud (id, estado_solicitud) VALUES (?,?)
           '''
    
    cursor = conn.execute(sql, (id, estado_sol))

    conn.commit()

    return jsonify({ 'msg': cursor.lastrowid })

  if request.method == 'GET':

    cursor = conn.execute('SELECT * FROM estado_solicitud')

    estados = cursor.fetchall()

    return jsonify({ 'estados_solicitud': estados })
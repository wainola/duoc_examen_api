import sqlite3
import os
from flask import request, jsonify, Blueprint

login = Blueprint('login', __name__)

current_directory = os.getcwd()

DB_PATH = f'{current_directory}/db/db_examen.db'

@login.route('/login', methods=['POST'])
def getCredentials():
  if request.method == 'POST':
    credentials = request.get_json()

    rut = credentials['credentials']['rut']
    password = credentials['credentials']['password']
    
    conn = sqlite3.connect(DB_PATH)
    estado = 'PENDIENTE'

    sql = '''
          SELECT rut, password FROM usuario WHERE rut = ?
          '''

    cursor = conn.execute(sql, (rut,))
    if len(cursor.fetchall()) == 0:
      return jsonify({ 'msg': 'no hay usuarios en la base de datos', 'status': 404})
    else:
      return jsonify({ 'msg': 'usuario encontrado', 'status': 200})

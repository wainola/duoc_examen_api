import sqlite3
import os
from flask import request, jsonify, Blueprint

login = Blueprint('login', __name__)

current_directory = os.getcwd()

DB_PATH = f'{current_directory}/db/db_examen.db'
conn = sqlite3.connect(DB_PATH)

@login.route('/login', methods=['POST'])
def getCredentials():
  if request.method == 'POST':
    credentials = request.get_json()

    rut = credentials['credentials']['rut']
    password = credentials['credentials']['password']
    
    estado = 'PENDIENTE'

    sql = '''
          SELECT nombre, apellido_paterno, apellido_materno, rut, password FROM usuario WHERE rut = ?
          '''

    cursor = conn.execute(sql, (rut,))
    result = cursor.fetchall()
    if len(result) != 0:
      data = result[0]
      user = {
        "nombre": data[0],
        "apellido_paterno": data[0],
        "apellido_materno": data[2],
        "rut": data[3],
        "password": data[4]
      }
      if user['password'] == password:
        return jsonify({ 'user': user, 'auth': True, 'status': 200 })
      else:
        return jsonify({ 'msg': 'contraseñas no coinciden', 'auth': False, 'status': 206})
    if len(result) == 0:
      return jsonify({ 'msg': 'usuario no encontrado', 'status': 404})

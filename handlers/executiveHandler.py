import sqlite3
import os
from flask import jsonify, Blueprint, request

executive = Blueprint('executive', __name__)

current_directory = os.getcwd()
DB_PATH = f'{current_directory}/db/db_examen.db'

conn = sqlite3.connect(DB_PATH)

@executive.route('/executive', methods=['POST', 'GET', 'DELETE'])
def ejecutivos():
  if request.method == 'POST':
    executive = request.get_json()['executive']

    id = executive['id']
    rut = executive['rut']
    dv = executive['dv']
    nombre = executive['nombre']
    apellido_paterno = executive['apellido_paterno']
    apellido_materno = executive['apellido_materno']
    fecha_nacimiento = executive['fecha_nacimiento']

    sql = '''
            INSERT INTO ejecutivo (id, rut, dv, nombre, apellido_paterno, apellido_materno, fecha_nacimiento) VALUES(?,?,?,?,?,?,?)
          '''

    cursor = conn.execute(sql, (id,rut,dv,nombre,apellido_paterno,apellido_materno,fecha_nacimiento,))

    conn.commit()

    return jsonify({ 'msg': cursor.lastrowid })

  if request.method == 'GET':

    cursor = conn.execute('SELECT * FROM ejecutivo')

    ejecutivos = cursor.fetchall()

    return jsonify({ 'ejecutivos': ejecutivos }) 

  if request.method == 'DELETE':
    
    id_ejecutivo = request.get_json()['executive']['id']

    cursor = conn.execute('DELETE FROM ejecutivo WHERE id = ?', (id_ejecutivo,))

    cur_row_count = cursor.rowcount

    conn.commit()

    if cur_row_count == 1:
      return jsonify({'executive_deleted': True})
    if cur_row_count == 0:
      return jsonify({'executive_deteled': False})

@executive.route('/login-executive', methods=['POST'])
def loginExecutive():
  if request.method == 'POST':
    credentials = request.get_json()

    rut = credentials['credentials']['rut']
    password = credentials['credentials']['password']

    sql = '''
          SELECT nombre, apellido_paterno, apellido_materno, rut, dv, password FROM ejecutivo WHERE rut = ?
          '''

    cursor = conn.execute(sql, (rut,))
    result = cursor.fetchall()
    if len(result) != 0:
      data = result[0]
      user = {
        "nombre": data[0],
        "apellido_paterno": data[1],
        "apellido_materno": data[2],
        "rut": f'{data[3]}-{data[4]}'
      }
      password_to_compare = data[5]
      if password_to_compare == password:
        return jsonify({ "user": user, "auth": True, "status": 200 })
      else:
        return jsonify({ "msg": "contraseñas no coinciden", "auth": False, "status": 206})
    if len(result) == 0:
      return jsonify({ "msg": "usuario no encontrado", "status": 404 })
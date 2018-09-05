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
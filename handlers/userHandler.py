import sqlite3
import os
from flask import jsonify, Blueprint, request


user = Blueprint('user', __name__)

current_directory = os.getcwd()
DB_PATH = f'{current_directory}/db/db_examen.db'

@user.route('/user', methods=['POST', 'GET', 'DELETE', 'PUT'])
def usuarios():
  if request.method == 'POST':
    user = request.get_json()

    id = user['user']['id']
    rut = user['user']['rut']
    dv = user['user']['dv']
    nombre = user['user']['nombre']
    apellido_paterno = user['user']['apellido_paterno']
    apellido_materno = user['user']['apellido_materno']
    fecha_nacimiento = user['user']['fecha_nacimiento']
    password = user['user']['password']
    sexo = user['user']['sexo']
    estado_civil = user['user']['estado_civil']
    hijos = user['user']['hijos']
    telefono = user['user']['telefono']
    email = user['user']['email']
    direccion = user['user']['direccion']
    comuna = user['user']['comuna']
    educacion = user['user']['educacion']
    renta = user['user']['renta']
    sueldo_liquido = user['user']['sueldo_liquido']
    enfermedad_cronica = user['user']['enfermedad_cronica']

    conn = sqlite3.connect(DB_PATH)

    query = f'INSERT INTO usuario (id, rut, dv, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, password, sexo, estado_civil, hijos, telefono, email, direccion, comuna, educacion, renta, sueldo_liquido, enfermedad_cronica) values ("{id}", "{rut}", "{dv}", "{nombre}", "{apellido_paterno}", "{apellido_materno}", "{fecha_nacimiento}", "{password}", "{sexo}", "{estado_civil}", "{hijos}", "{telefono}", "{email}", "{direccion}", "{comuna}", "{educacion}", "{renta}", "{sueldo_liquido}", "{enfermedad_cronica}")'

    cursor = conn.execute(query)

    conn.commit()

    return jsonify({ 'msg': cursor.lastrowid})


  if request.method == 'GET':

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.execute('SELECT * FROM usuario')

    usuarios = cursor.fetchall()

    return jsonify({'usuarios': usuarios})

  if request.method == 'DELETE':

    id_user = request.get_json()['user']['id']

    conn = sqlite3.connect(DB_PATH)

    delete_query = f'DELETE FROM usuario WHERE id = "{id_user}"'

    cursor = conn.execute(delete_query)

    cur_row_count = cursor.rowcount

    conn.commit()

    if cur_row_count == 1:
      return jsonify({ 'user_deleted': True })
    
    if cur_row_count == 0:
      return jsonify({ 'user_deleted': False })

    
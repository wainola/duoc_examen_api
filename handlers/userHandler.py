import sqlite3
import os
from flask import jsonify, Blueprint, request


user = Blueprint('user', __name__)

current_directory = os.getcwd()
DB_PATH = f'{current_directory}/db/db_examen.db'

conn = sqlite3.connect(DB_PATH)

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

    query = f'INSERT INTO usuario (id, rut, dv, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, password, sexo, estado_civil, hijos, telefono, email, direccion, comuna, educacion, renta, sueldo_liquido, enfermedad_cronica) values ("{id}", "{rut}", "{dv}", "{nombre}", "{apellido_paterno}", "{apellido_materno}", "{fecha_nacimiento}", "{password}", "{sexo}", "{estado_civil}", "{hijos}", "{telefono}", "{email}", "{direccion}", "{comuna}", "{educacion}", "{renta}", "{sueldo_liquido}", "{enfermedad_cronica}")'

    cursor = conn.execute(query)

    conn.commit()

    return jsonify({ 'msg': cursor.lastrowid})


  if request.method == 'GET':

    cursor = conn.execute('SELECT * FROM usuario')

    usuarios = cursor.fetchall()

    return jsonify({'usuarios': usuarios})

  if request.method == 'DELETE':

    id_user = request.get_json()['user']['id']

    delete_query = f'DELETE FROM usuario WHERE id = "{id_user}"'

    cursor = conn.execute(delete_query)

    cur_row_count = cursor.rowcount

    conn.commit()

    if cur_row_count == 1:
      return jsonify({ 'user_deleted': True })
    
    if cur_row_count == 0:
      return jsonify({ 'user_deleted': False })

  if request.method === 'PUT':

    user = request.get_json()['user']
    estado_solicitud = request.get_json()['request_status']

    id = user['id']
    rut = user['rut']
    dv = user['dv']
    nombre = user['nombre']
    apellido_paterno = user['apellido_paterno']
    apellido_materno = user['apellido_materno']
    fecha_nacimiento = user['fecha_nacimiento']
    sexo = user['sexo']
    estado_civil = user['estado_civil']
    hijos = user['hijos']
    telefono = user['telefono']
    email = user['email']
    direccion = user['direccion']
    comuna = user['comuna']
    educacion = user['educacion']
    renta = user['renta']
    sueldo_liquido = user['sueldo_liquido']
    enfermedad_cronica = user['enfermedad_cronica']

    id_estado_solicitud = estado_solicitud['id']
    nuevo_estado_solicitud = estado_solicitud['nuevo_estado']

    sql_user = '''
          UPDATE usuario SET rut = ?, dv = ?, nombre = ?, apelllido_paterno = ?, apellido_materno = ?, fecha_nacimiento = ?, sexo = ?, estado_civil = ?, hijos = ?, telefono = ?, email = ?, direccion = ?, comuna = ?, educacion = ?, renta = ?, sueldo_liquido = ?, enfermedad_cronica = ? WHERE id = ?
          '''

    sql_request_status = '''
                          UPDATE estado_solicitud SET estado_solicitud = ? WHERE id = ?
                         '''

    cur_user = conn.execute(sql_user, (rut, dv, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado_civil, hijos, telefono, email, direccion, comuna, educacion, renta, sueldo_liquido, enfermedad_cronica, id)) 

    cur_request = conn.execute(sql_request_status, (nuevo_estado_solicitud, id_estado_solicitud))

    conn.commit()

    return jsonify({ 'msg': 'solicitud actualizada', 'status': 200 })
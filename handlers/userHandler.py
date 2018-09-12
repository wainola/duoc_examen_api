import sqlite3
import os
from flask import jsonify, Blueprint, request

user = Blueprint('user', __name__)

current_directory = os.getcwd()
DB_PATH = f'{current_directory}/db/db_examen.db'

conn = sqlite3.connect(DB_PATH)

@user.route('/create-resquest', methods=['POST'])
def create_request():

  # CREATE USER
  if request.method == 'POST':
    user = request.get_json()
    estado_sol = request.get_json()['estado_solicitud']
    credito = request.get_json()['credito']

    id = user['user']['id']
    rut = user['user']['rut']
    dv = user['user']['dv']
    nombre = user['user']['nombre']
    apellido_paterno = user['user']['apellido_paterno']
    apellido_materno = user['user']['apellido_materno']
    fecha_nacimiento = user['user']['fecha_nacimiento']
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
    role = user['user']['role']

    id_estado = estado_sol['id']
    estado = estado_sol['estado_solicitud']

    id_credito = credito['id']

    sql = '''
          INSERT INTO usuario (id, rut, dv, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado_civil, hijos, telefono, email, direccion, comuna, educacion, renta, sueldo_liquido, enfermedad_cronica, role) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
          '''
    sql_request_status = '''
                          INSERT INTO estado_solicitud (id, estado_solicitud) VALUES (?, ?)
                         '''

    sql_credito = '''
                  INSERT INTO credito (id, fk_usuario_id, fk_estado_solicitud_id) VALUES (?,?,?)
                  '''

    cursor = conn.execute(sql, (id, rut, dv, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado_civil, hijos, telefono, email, direccion, comuna, educacion, renta, sueldo_liquido, enfermedad_cronica, role,))

    cur_request = conn.execute(sql_request_status, (id_estado, estado,))

    cur_credito = conn.execute(sql_credito, (id_credito, id, id_estado,))

    conn.commit()

    return jsonify({ 'msg': cursor.lastrowid})

@user.route('/user', methods=['GET', 'DELETE', 'PUT'])
def get_users():
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

  # UPDATE USERS
  if request.method == 'PUT':

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

@user.route('/getAll', methods=['GET'])
def getAllData():
    if request.method == 'GET':
      cursor = conn.execute('SELECT usuario.*, estado_solicitud.* FROM usuario JOIN credito ON usuario.id = credito.fk_usuario_id JOIN estado_solicitud on credito.fk_estado_solicitud_id = estado_solicitud.id')

      usuarios = []
      allUserData = []
      for row in cursor:
        usuarios.append({ 'id': row[0], 'rut': f'{row[1]}-{row[2]}', 'nombre': f'{row[3]} {row[4]} {row[5]}', 'estado': row[21]})
        allUserData.append({ 'id': row[0], 'rut': f'{row[1]}-{row[2]}', 'nombre': f'{row[3]} {row[4]} {row[5]}', 'estado': row[21], 'sexo': row[8], 'estado_civil': row[9], 'hijos': row[10], 'telfono': row[11], 'correo': row[12], 'direccion': row[13], 'comuna': row[14], 'educacion': row[15], 'renta': row[16], 'sueldo_liquido': row[17], 'enfermedad_cronica': row[18], 'estado_solicitud': row[21], 'id_solicitud': row[20]})

      return jsonify({'usuarios': usuarios, 'all_user_data': allUserData })
import sqlite3
import os
from flask import jsonify, Blueprint, request
signup = Blueprint('signup', __name__)

current_directory = os.getcwd()
DB_PATH = f'{current_directory}/db/db_examen.db'

conn = sqlite3.connect(DB_PATH, check_same_thread=False)

@signup.route('/signup', methods=['POST'])
def registro():
  if request.method == 'POST':
    registro = request.get_json()['new_user']

    id = registro['id']
    rut = registro['rut']
    dv = registro['dv']
    nombre = registro['nombre']
    apellido_paterno = registro['apellido_paterno']
    apellido_materno = registro['apellido_materno']
    fecha_nacimiento = registro['fecha_nacimiento']
    password = registro['password']

    sql = '''
          INSERT INTO usuario (id, rut, dv, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, password) VALUES (?,?,?,?,?,?,?,?)
          '''

    cursor = conn.execute(sql, (id,rut,dv,nombre,apellido_paterno,apellido_materno,fecha_nacimiento,password,))

    conn.commit()

    return jsonify({'msg': cursor.lastrowid, "status": 201})

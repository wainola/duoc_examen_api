import sqlite3
import os
from flask import jsonify, Blueprint, request


user = Blueprint('user', __name__)

@user.route('/user', methods=['POST', 'GET'])
def create():
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
    return jsonify({ 'msg': sueldo_liquido})
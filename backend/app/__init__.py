# Libraries
from flask_cors import CORS
from .utilities import *
import boto3
from boto3.dynamodb.conditions import Key, Attr

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    abort,
    session,
)

import sys
import uuid
import json
import os
import requests
import time
from datetime import datetime
from datetime import timedelta

#credenciales de aws
url = 'https://eggmom.s3.amazonaws.com/credentials.txt'
r = requests.get(url)
texto = r.text

print(texto)


texto = texto.split('\n')
config = {}

for line in range(len(texto)):
    if line == 0:
        config['aws_access_key_id'] = texto[line].split('=')[1][0:-1]
    elif line == 1:
        config['aws_secret_access_key'] = texto[line].split('=')[1][0:-1]
    elif line == 2:
        config['aws_session_token'] = texto[line].split('=')[1]

print(config)
# wait for dynamodb to be ready
time.sleep(5)

# DynamoDB
dynamoDB = boto3.resource(
    'dynamodb', 
    aws_access_key_id=config['aws_access_key_id'], 
    aws_secret_access_key=config['aws_secret_access_key'], 
    aws_session_token=config['aws_session_token'],
    region_name='us-east-1'
    )
# App

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'pneumonoultramicroscopicsilicovolcanoconiosis'

    with app.app_context():
        CORS(app, origins=['http://hosteando' ,'http://3.212.47.164:3000', 'http://3.212.47.164:5000', 'http://3.212.47.164:8080'], supports_credentials=True)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    # ROUTES API -----------------------------------------------------------


    # GET ------------------------------------------------------------------

    @app.route('/empresa/<tenant_id>/sedes', methods=['GET']) # Listar sedes
    def get_sedes(tenant_id):
        code = 200
        partition_key = tenant_id
        try:
            table = dynamoDB.Table('Sede')
            response = table.scan(
                FilterExpression=Attr('tenant_id').eq(partition_key)
            )
            data = response['Items']
            if data:
                if len(data) == 0:
                    code = 404
                    message = "No hay sedes"
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
        except Exception as e:
            print(sys.exc_info())
            code = 500


        if code == 400:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code

    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/grupos', methods=['GET']) # Listar grupos
    def get_grupos(tenant_id, sede_id):
        code = 200
        partition_key = tenant_id + "+" + sede_id
        try:
            table = dynamoDB.Table('Grupos')
            response = table.scan(
                FilterExpression=Attr('tenant_id+sede_id').eq(partition_key)
            )
            data = response['Items']
            if data:
                if len(data) == 0:
                    code = 404
                    message = "No hay grupos"
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
        except Exception as e:
            print(sys.exc_info())
            code = 500


        if code == 400:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code
    
    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/grupos/<grupo_id>/objetos', methods=['GET']) # Listar objetos
    def get_objetos(tenant_id, sede_id, grupo_id):
        code = 200
        partition_key = tenant_id + "+" + sede_id + "+" + grupo_id
        try:
            table = dynamoDB.Table('Objetos')
            response = table.scan(
                FilterExpression=Attr('tenant_id+sede_id+grupo_id').eq(partition_key)
            )
            data = response['Items']
            if data:
                if len(data) == 0:
                    code = 404
                    message = "No hay objetos"
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
        except Exception as e:
            print(sys.exc_info())
            code = 500


        if code == 400:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code
        
    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/grupos/<grupo_id>/objetos/<objeto_id>/registros', methods=['GET']) # Listar registros
    def get_registros(tenant_id, sede_id, grupo_id, objeto_id):
        code = 200
        partition_key = tenant_id + "+" + sede_id + "+" + grupo_id + "+" + objeto_id
        try:
            table = dynamoDB.Table('Registros')
            response = table.scan(
                FilterExpression=Attr('tenant_id+sede_id+grupo_id+objeto_id').eq(partition_key)
            )
            data = response['Items']
            data = sorted(data, key=lambda k: k['fecha_hora'], reverse=False)
            if data:
                if len(data) == 0:
                    code = 404
                    message = "No hay registros"
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
        except Exception as e:
            print(sys.exc_info())
            code = 500


        if code == 400:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code


    # Especific GET --------------------------------------------------------

    @app.route('/empresa/<tenant_id>', methods=['GET']) # Listar sedes
    def get_empresa(tenant_id):
        code = 200
        partition_key = tenant_id
        try:
            table = dynamoDB.Table('Empresas')
            response = table.scan(
                FilterExpression=Attr('tenant_id').eq(partition_key)
            )
            data = response['Items']
            if data:
                if len(data) == 0:
                    code = 404
                    message = "No hay empresa"
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
        except Exception as e:
            print(sys.exc_info())
            code = 500


        if code == 400:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code

    @app.route('/empresa/<tenant_id>/sedes/<sede_id>', methods=['GET']) # Listar sedes
    def get_sede(tenant_id, sede_id):
        code = 200
        partition_key = tenant_id
        sorted_key = sede_id
        try:
            table = dynamoDB.Table('Sede')
            response = table.scan(
                FilterExpression=Attr('tenant_id').eq(partition_key) & Attr('sede_id').eq(sorted_key)
            )
            data = response['Items']
            if data:
                if len(data) == 0:
                    code = 404
                    message = "No hay sede"
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
        except Exception as e:
            print(sys.exc_info())
            code = 500


        if code == 400:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code

    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/grupos/<grupo_id>', methods=['GET']) # Listar sedes
    def get_grupo(tenant_id, sede_id, grupo_id):
        code = 200
        partition_key = tenant_id + "+" + sede_id
        sorted_key = grupo_id
        try:
            table = dynamoDB.Table('Grupos')
            response = table.scan(
                FilterExpression=Attr('tenant_id+sede_id').eq(partition_key) & Attr('grupo_id').eq(sorted_key)
            )
            data = response['Items']
            if data:
                if len(data) == 0:
                    code = 404
                    message = "No hay grupo"
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
        except Exception as e:
            print(sys.exc_info())
            code = 500


        if code == 400:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code
        
    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/grupos/<grupo_id>/objetos/<objeto_id>', methods=['GET']) 
    def get_objeto(tenant_id, sede_id, grupo_id, objeto_id):
        code = 200
        partition_key = tenant_id + "+" + sede_id + "+" + grupo_id
        sorted_key = objeto_id
        try:
            table = dynamoDB.Table('Objetos')
            response = table.scan(
                FilterExpression=Attr('tenant_id+sede_id+grupo_id').eq(partition_key) & Attr('objeto_id').eq(sorted_key)
            )
            data = response['Items']
            if data:
                if len(data) == 0:
                    code = 404
                    message = "No hay objeto"
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
        except Exception as e:
            print(sys.exc_info())
            code = 500


        if code == 400:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code
    
    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/grupos/<grupo_id>/objetos/<objeto_id>/registros/<registro_id>', methods=['GET']) 
    def get_registro(tenant_id, sede_id, grupo_id, objeto_id, registro_id):
        code = 200
        partition_key = tenant_id + "+" + sede_id + "+" + grupo_id + "+" + objeto_id
        sorted_key = registro_id
        try:
            table = dynamoDB.Table('Registros')
            response = table.scan(
                FilterExpression=Attr('tenant_id+sede_id+grupo_id+objeto_id').eq(partition_key) & Attr('registro_id').eq(sorted_key)
            )
            data = response['Items']
            if data:
                if len(data) == 0:
                    code = 404
                    message = "No hay registro"
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
        except Exception as e:
            print(sys.exc_info())
            code = 500

        if code == 400:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            data = data[0]
            return jsonify({"success": True, "data": data}), code


    # obtener objetos de todos los grupos de una sede
    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/objetos', methods=['GET'])
    def get_objetos_sede(tenant_id, sede_id):
        code = 200
        partition_key = tenant_id + "+" + sede_id
        try:
            table = dynamoDB.Table('Objetos')
            # si su tenant_id+sede_id+grupo_id contiene partition_key
            response = table.scan(
                FilterExpression=Attr('tenant_id+sede_id+grupo_id').contains(partition_key)
            )

            data = response
            if data:
                data = response['Items']
                if len(data) == 0:
                    code = 404
                    message = "No hay objetos"
                    return jsonify({"success": False, "message": message}), code
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
                return jsonify({"success": False, "message": message}), code
        except Exception as e:
            print(sys.exc_info())
            code = 500

        if code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code


    # obtener arduinos disponibles
    @app.route('/empresa/<tenant_id>/arduinos', methods=['GET']) 
    def get_arduinos(tenant_id):
        code = 200
        partition_key = tenant_id
        try:
            table = dynamoDB.Table('Arduinos')
            response = table.scan(
                FilterExpression=Attr('tenant_id').eq(partition_key)
            )
            data = response['Items']
        except Exception as e:
            print(sys.exc_info())
            code = 500

        if code == 400:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code 


    # POST -----------------------------------------------------------------

    # create group
    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/grupos', methods=['POST'])
    def create_grupo(tenant_id, sede_id):
        code = 200
        try:
            data = request.json
            table = dynamoDB.Table('Grupos')
            item = {
                'tenant_id+sede_id': tenant_id + "+" + sede_id,
                'grupo_id': data['nombre'],
                'humedad': {
                    'min': data['humedad_min'],
                    'max': data['humedad_max']
                },
                'temperatura': {
                    'min': data['temperatura_min'],
                    'max': data['temperatura_max']
                }
            }
            table.put_item(Item=item)
            data = item
        except Exception as e:
            print(sys.exc_info())
            code = 500
        if code == 400:
            return jsonify({"success": False, "message": message}), code
        elif code == 409:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code

    # create object
    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/grupos/<grupo_id>/objetos', methods=['POST'])
    def create_objeto(tenant_id, sede_id, grupo_id):
        code = 200
        try:
            data = request.json
            table = dynamoDB.Table('Objetos')
            item = {
                'tenant_id+sede_id+grupo_id': tenant_id + "+" + sede_id + "+" + grupo_id,
                'objeto_id': data['nombre'],
                'ARDUINO_ID': data['arduino_id'],
            }

            #revisar el grupo
            table = dynamoDB.Table('Grupos')
            response = table.scan(
                FilterExpression=Attr('tenant_id+sede_id').eq(tenant_id + "+" + sede_id) & Attr('grupo_id').eq(grupo_id)
            )

            grupo = response['Items']
            if grupo:
                if len(grupo) == 0:
                    return jsonify({"success": False, "message": "No existe el grupo"}), 400
                else:
                    grupo = grupo[0]

            # revisar si existe el arduino_id
            table = dynamoDB.Table('Arduinos')
            # scan by tenant_id and arduino_id
            response = table.scan(
                FilterExpression=Attr('tenant_id').eq(tenant_id) & Attr('ARDUINO_ID').eq(data['arduino_id']) & Attr('available').eq(True)
            )

            arduino = response

            if arduino:
                arduino = response['Items']
                if len(arduino) == 0:
                    return jsonify({"success": False, "message": "No existe el arduino"}), 400
                else:
                    arduino = arduino[0]
                    arduino['available'] = False
                    table.put_item(Item=arduino)
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
                return jsonify({"success": False, "message": message}), code

            
            # revisar si existe el grupo_id
            table = dynamoDB.Table('Objetos')
            table.put_item(Item=item)
            data = item
        except Exception as e:
            print(sys.exc_info())
            code = 500
    
        if code == 400:

            return jsonify({"success": False, "message": message}), code
        elif code == 409:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data}), code


    # get sede_id
    @app.route('/empresa/<tenant_id>/login', methods=['POST'])
    def login(tenant_id):
        code = 200
        try:
            data = request.json

            tableSedes = dynamoDB.Table('Sede')
            response = tableSedes.scan(
                FilterExpression=Attr('tenant_id').eq(tenant_id) & Attr('Nombre').eq(data['name'])
            )

            sede = response
            if sede:
                sede = response['Items']
                if len(sede) == 0:
                    return jsonify({"success": False, "message": "No existe la sede"}), 400
                else:
                    if sede[0]['sede_id'] != data['password']:
                        return jsonify({"success": False, "message": "Contraseña incorrecta"}), 400
                    else:
                        sede = sede[0]
            else:
                code = 404
                message = "No se pudo acceder a la tabla"
                return jsonify({"success": False, "message": message}), code

        except Exception as e:
            print(sys.exc_info())
            code = 500
    
        if code == 400:

            return jsonify({"success": False, "message": message}), code
        elif code == 409:
            return jsonify({"success": False, "message": message}), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({"success": True, "data": data, "token": sede['sede_id']}), code

    #ruta para suscribir un correo
    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/suscribir/<email>', methods=['POST'])
    def suscribir(tenant_id, sede_id, email):
        code = 200
        aws_access_key_id = config['aws_access_key_id']
        aws_secret_access_key = config['aws_secret_access_key']
        aws_session_token = config['aws_session_token']
        region = 'us-east-1'
        
        try:
            # Crear un cliente SNS utilizando boto3 y las credenciales proporcionadas
            sns_client = boto3.client('sns', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token, region_name=region)

            # ARN del tema al que deseas suscribirte
            topic_arn = "arn:aws:sns:us-east-1:859485701311:RegisterSender"

            # Dirección del endpoint al que se enviarán las notificaciones
            correo = email

            # Configurar la suscripción utilizando el cliente SNS
            response = sns_client.subscribe(
                TopicArn=topic_arn,
                Protocol="email",
                Endpoint=correo
            )

            # Imprimir la respuesta del servidor
            print(response)
            data = response
        except Exception as e:
            print(sys.exc_info())
            code = 500
            return jsonify({"success": False, "message": "No se pudo suscribir el correo"}), code

        return jsonify({"success": True, "data": response}), code


    # HANDLE ERROR ---------------------------------------------------------
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "message": 'Resource not found'}), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"success": False, "message": 'Unauthorized'}), 401

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "message": 'Bad request'}), 400

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({"success": False, "message": 'Method not allowed'}), 405

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({"success": False, "message": 'Forbidden'}), 403

    @app.errorhandler(409)
    def conflict(error):
        return jsonify({"success": False, "message": 'Conflict'}), 409

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"success": False, "message": 'Server error'}), 500

    @app.errorhandler(501)
    def not_implemented(error):
        return jsonify({"success": False, "message": 'Not implemented'}), 501

    return app

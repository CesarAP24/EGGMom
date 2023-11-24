# Libraries
from flask_cors import CORS
from .utilities import *
from config.local import config
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
from datetime import datetime
from datetime import timedelta


dynamoDB = boto3.resource(
    'dynamodb', 
    aws_access_key_id=config['aws_access_key_id'], 
    aws_secret_access_key=config['aws_secret_access_key'], 
    aws_session_token=config['aws_session_token'], 
    region_name=config['region']
    )
# App

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'pneumonoultramicroscopicsilicovolcanoconiosis'

    with app.app_context():
        
        CORS(app, origins="*", supports_credentials=True)

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
            data = sorted(data, key=lambda k: k['fecha_hora'], reverse=True)
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
        
    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/grupos/<grupo_id>/objetos/<objeto_id>', methods=['GET']) # Listar sedes
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
    
    @app.route('/empresa/<tenant_id>/sedes/<sede_id>/grupos/<grupo_id>/objetos/<objeto_id>/registros/<registro_id>', methods=['GET']) # Listar sedes
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

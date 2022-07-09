'''
utils.py: Modulo para definir los metodos de funcionalidad auxiliar
'''
from flask import jsonify
from cerberus import Validator
from flask_jwt_extended import create_access_token

def json_message(msg):
    '''
    Metodo que devuelve un mensaje en formato json
    '''
    return jsonify({
        "msg": msg
    }), 200

def json_message_custom_code(msg, code):
    return jsonify({
        "msg": msg
    }), code

def json_message_error_code(msg):
    return jsonify({
        "msg": msg
    }), 400

def validate_parameters(parameters, schema):
    v = Validator(schema)
    v.allow_unknown = True
    if not v.validate(parameters):
        return jsonify({
            "errors": v.errors
        }), 400

def create_jwt(id, email):
    jwt_token_identity = {
        'id': id,
        'email': email
    }

    access_token = create_access_token(identity=jwt_token_identity)
    return access_token
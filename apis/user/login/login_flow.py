from os import access
from flask import jsonify
from flask_jwt_extended import create_access_token
from utils.utils import create_jwt, json_message
from models.user import User


class LoginFlow:

    def __call__(self, request, bcrypt):

        user_email = request.json['email']
        user_password = request.json['password']

        user_obj = User.objects(
            email=user_email
        ).first()

        if user_obj is not None:
            if bcrypt.check_password_hash(user_obj.to_json()['password'], user_password):
                access_token = create_jwt(user_obj.to_json()['id'], user_obj.to_json()['email'])
                return jsonify({
                    "token": access_token,
                    "user": user_obj.to_json()
                })

            return json_message("Contraseña incorrecta")

        return json_message("El usuario no está registrado")

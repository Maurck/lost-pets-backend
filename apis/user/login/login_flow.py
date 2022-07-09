from flask import jsonify
from utils.utils import create_jwt, json_message_error_code
from models.user import User


class LoginFlow:

    def __call__(self, request, bcrypt):

        user_email = request.json['email']
        user_password = request.json['password']

        user_obj = User.objects(
            email=user_email
        ).first()

        if user_obj is None:
            return json_message_error_code("El usuario no está registrado")

        if bcrypt.check_password_hash(user_obj.to_json()['password'], user_password):
            access_token = create_jwt(user_obj.to_json()['id'], user_obj.to_json()['email'])
            return jsonify({
                "token": access_token,
                "user": user_obj.to_json()
            })

        return json_message_error_code("Contraseña incorrecta")

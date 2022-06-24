'''
register.py: Modulo para el registro
'''
from flask import jsonify
from utils.utils import json_message, create_jwt
from models.user import User


class RegisterFlow:
    '''
    Clase que registra a un usuario
    '''
    def __call__(self, request, bcrypt):

        req_user_email = request.json['email']

        user_obj = User.objects(
            email=req_user_email
        ).first()

        if user_obj is None:
            new_user = User(
                name=request.json['name'],
                password=bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
                email=req_user_email,
                mother_lastname=request.json['mother_lastname'],
                father_lastname=request.json['father_lastname'],
                address=request.json['address'],
                dni=request.json['dni'],
                phone_number=request.json['phone_number'],
                nickname=request.json['nickname']
            )

            new_user.save()

            access_token = create_jwt(new_user.to_json()["id"], new_user.to_json()["email"])
            return jsonify({
                "msg": "Usuario registrado",
                "token": access_token,
                "user": new_user.to_json()
            })

        return json_message("Usuario ya registrado")

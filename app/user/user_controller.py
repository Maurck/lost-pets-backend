from flask import request
from flask_restx import Resource

from .dto.user_dto import UserDto
from .user_service import save_new_user, get_all_users, get_a_user

user_ns = UserDto.user_ns
_user = UserDto.user


@user_ns.route('/')
class UserApi(Resource):
    @user_ns.doc('Lista de usuarios')
    @user_ns.marshal_list_with(_user, envelope='users')
    def get(self):
        """Lista de usuarios"""
        return get_all_users()

    @user_ns.response(201, 'Usuario creado con exito')
    @user_ns.doc('Crear un nuevo usuario')
    @user_ns.expect(_user, validate=True)
    def post(self):
        """Crear un nuevo usuario """
        body = request.json
        print(body)
        return save_new_user(body=body)
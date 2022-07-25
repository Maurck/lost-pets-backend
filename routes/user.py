'''
user.py: Modulo para definir las rutas relacionadas con la API User
'''
from flask import request
from flask_jwt_extended import jwt_required
from apis.user.delete_user.delete_user import DeleteUser

from apis.user.delete_users.delete_users import DeleteUsers
from apis.user.login.login import Login
from apis.user.register.register import Register
from apis.user.get_user.get_user import GetUser
from apis.user.get_users.get_users import GetUsers


def create_routes_user(app, bcrypt):
    '''
    Metodo que crea las rutas relacionadas con la API User
    '''
    # pylint: disable=unused-variable
    @app.route('/register', methods=['POST'])
    def register():
        register = Register()
        return register(request, bcrypt)

    # pylint: disable=unused-variable
    @app.route('/login', methods=['POST'])
    def login():
       login = Login()
       return login(request, bcrypt)

    @app.route('/users', methods=['DELETE'])
    @jwt_required()
    def delete_users():
        delete_users = DeleteUsers()
        return delete_users(request)

    # pylint: disable=unused-variable
    @app.route('/user')
    @jwt_required()
    def get_user():
        get_user = GetUser()
        return get_user(request)

    
    # pylint: disable=unused-variable
    @app.route('/users')
    @jwt_required()
    def get_users():
        get_users = GetUsers()
        return get_users(request)

    @app.route('/user', methods=['DELETE'])
    @jwt_required()
    def delete_user():
        delete_user = DeleteUser()
        return delete_user(request)

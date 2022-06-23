from flask_restx import Namespace, fields

class UserDto:
    user_ns = Namespace('User', description='Operaciones de usuario')
    user = user_ns.model('User', {
        'id': fields.String(required=True, description='Id de usuario'),
        'name': fields.String(required=True, description='Nombre real del usuario'),
        'father_lastname': fields.String(required=True, description='Apellido paterno del usuario'),        
        'mother_lastname': fields.String(required=True, description='Apellido materno del usuario'),
        'address': fields.String(required=True, description='Dirección del usuario'),
        'dni': fields.String(required=True, description='DNI del usuario'),
        'email': fields.String(required=True, description='Email del usuario'),
        'phone_number': fields.String(required=True, description='Numero de telefono del usuario'),
        'nickname': fields.String(required=True, description='Nombre del usuario en la aplicación')
    })
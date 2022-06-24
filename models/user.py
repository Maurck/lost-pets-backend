'''
user.py: Modulo para definir el modelo Usuario
'''
from mongoengine import Document, StringField


class User(Document):
    '''
    Clase que define el modelo usuario
    '''
    name = StringField(required=True)
    password = StringField(required=True)
    email = StringField(required=True)
    mother_lastname = StringField(required=True)
    father_lastname = StringField(required=True)
    address = StringField(required=True)
    dni = StringField(required=True)
    phone_number = StringField(required=True)
    nickname = StringField(required=True)

    def to_json(self):
        '''
        Metodo que devuelve los atributos de la clase en formato json
        '''
        user_dict = {
            'id': str(self.pk),
            "name": self.name,
            "mother_lastname": self.mother_lastname,
            "father_lastname": self.father_lastname,
            "address": self.address,
            "dni": self.dni,
            "email": self.email,
            "password": self.password,
            "phone_number": self.phone_number,
            "nickname": self.nickname
        }
        return user_dict
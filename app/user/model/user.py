'''
user.py: Modulo para definir el modelo Usuario
'''
from mongoengine import Document, StringField, DateTimeField, BooleanField


class User(Document):
    '''
    Clase que define el modelo usuario
    '''
    name = StringField(required=True)
    mother_lastname = StringField(required=False, default="")
    father_lastname = StringField(required=False, default="")
    address = StringField(required=False, default="")
    dni = StringField(required=False, default="")
    email = StringField(required=False, default="")
    phone_number = StringField(required=False, default="")
    nickname = StringField(required=False, default="")

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
            "phone_number": self.phone_number,
            "nickname": self.nickname
        }
        return user_dict
'''
pet.py: Modulo para definir el modelo Mascota
'''
from datetime import date
from mongoengine import Document, StringField, DateField, ObjectIdField


class Pet(Document):
    '''
    Clase que define el modelo mascota
    '''
    name = StringField(required=True)
    gender = StringField(required=True)
    birthdate = DateField(required=True)
    registered_at = DateField(required=False, default=date.today().strftime("%d-%m-%Y"))
    color = StringField(required=True)
    breed = StringField(required=True)
    characteristics = StringField(required=True)
    size = StringField(required=True)
    owner_id = ObjectIdField(required=True)

    def to_json(self):
        '''
        Metodo que devuelve los atributos de la clase en formato json
        '''
        user_dict = {
            'id': str(self.pk),
            "name": self.name,
            "gender": self.gender,
            "birthdate": self.birthdate,
            "registered_at": self.registered_at,
            "color": self.color,
            "breed": self.breed,
            "characteristics": self.characteristics,
            "size": self.size,
            "owner_id": str(self.owner_id)
        }
        return user_dict
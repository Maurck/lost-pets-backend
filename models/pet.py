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
    owner_name = StringField(required=True, default="Sin dueño")
    img_url = StringField(required=True)
    img_public_id = StringField(required=True)
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
        pet_dict = {
            'id': str(self.pk),
            "name": self.name,
            "owner_name": self.owner_name,
            "img_url": self.img_url,
            "img_public_id": self.img_public_id,
            "gender": self.gender,
            "birthdate": self.birthdate,
            "registered_at": self.registered_at,
            "color": self.color,
            "breed": self.breed,
            "characteristics": self.characteristics,
            "size": self.size,
            "owner_id": str(self.owner_id)
        }
        return pet_dict
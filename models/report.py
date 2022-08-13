from mongoengine import Document, StringField


class Report(Document):
    '''
    Clase que define el modelo reporte
    '''
    address = StringField(required=True)
    description = StringField(required=True)
    reported_img_url = StringField(required=True)
    reported_img_public_id = StringField(required=True)
    pet_id = StringField(required=True)
    reporter_id = StringField(required=True)

    def to_json(self):
        '''
        Metodo que devuelve los atributos de la clase en formato json
        '''
        report = {
            'id': str(self.pk),
            "address": self.address,
            "description": self.description,
            "reported_img_url": self.reported_img_url,
            "reported_img_public_id": self.reported_img_public_id,
            "pet_id": self.pet_id,
            "reporter_id": self.reporter_id
        }
        return report
'''
register.py: Modulo para el registro
'''
from flask import jsonify
from models.pet import Pet
from models.user import User
from utils.utils import json_message_error_code


class RegisterPetFlow:
    '''
    Clase que registra a una mascota
    '''
    def __call__(self, request):

        owner_id = request.json['owner_id']

        owner: User = User.objects(
            id=owner_id
        ).first()

        if owner is None:
            return json_message_error_code("Dueño no existente")

        new_pet = Pet(
            name=request.json['name'],
            gender=request.json['gender'],
            birthdate=request.json['birthdate'],
            color=request.json['color'],
            breed=request.json['breed'],
            characteristics=request.json['characteristics'],
            size=request.json['size'],
            owner_id=owner_id,
            owner_name = owner.to_json()["name"] + " " + owner.to_json()["father_lastname"] + " " + owner.to_json()["mother_lastname"]  
        )

        new_pet.save()

        return jsonify({
            "msg": "Mascota registrada",
            "pet": new_pet.to_json()
        })

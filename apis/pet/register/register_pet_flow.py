'''
register.py: Modulo para el registro
'''
from flask import jsonify
from models.pet import Pet


class RegisterPetFlow:
    '''
    Clase que registra a una mascota
    '''
    def __call__(self, request):

        new_pet = Pet(
            name=request.json['name'],
            gender=request.json['gender'],
            birthdate=request.json['birthdate'],
            color=request.json['color'],
            breed=request.json['breed'],
            characteristics=request.json['characteristics'],
            size=request.json['size'],
            owner_id=request.json['owner_id']
        )

        new_pet.save()

        return jsonify({
            "msg": "Mascota registrada",
            "pet": new_pet.to_json()
        })

'''
register.py: Modulo para el registro
'''
from flask import jsonify
from models.pet import Pet
from models.user import User
from utils.utils import json_message_error_code
import cloudinary.uploader


class RegisterPetFlow:
    '''
    Clase que registra a una mascota
    '''
    def __call__(self, request):

        owner_id = request.form['owner_id']

        owner: User = User.objects(
            id=owner_id
        ).first()

        if owner is None:
            return json_message_error_code("Dueño no existente")

        pet_img = request.files['img']
        upload_data = cloudinary.uploader.upload(pet_img)
        print(upload_data)

        new_pet = Pet(
            name=request.form['name'],
            gender=request.form['gender'],
            birthdate=request.form['birthdate'],
            color=request.form['color'],
            breed=request.form['breed'],
            characteristics=request.form['characteristics'],
            size=request.form['size'],
            owner_id=owner_id,
            owner_name=owner.to_json()["name"] + " " + owner.to_json()["father_lastname"] + " " + owner.to_json()["mother_lastname"],
            img_url=upload_data["url"],
            img_public_id=upload_data["public_id"]
        )

        new_pet.save()

        return jsonify({
            "msg": "Mascota registrada",
            "pet": new_pet.to_json()
        })

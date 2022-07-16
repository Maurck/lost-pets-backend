from flask import jsonify
from models.pet import Pet
from utils.utils import json_message_error_code


class GetPetFlow:
    def __call__(self, request):

        pet_id = request.args.get('id')

        pet_obj = Pet.objects(
            id=pet_id
        ).first()

        if pet_obj is None:
            return json_message_error_code("Mascota no encontrada")

        return jsonify({"pet": pet_obj.to_json()})

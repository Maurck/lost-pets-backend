from flask import jsonify
from models.pet import Pet


class GetPetsFlow:

    def __call__(self):
        pets_list = Pet.objects()
        pets_jsons_list = []
        pets_jsons_list = list(map(lambda pet_obj: pet_obj.to_json(), pets_list))

        return jsonify({"pets": pets_jsons_list})


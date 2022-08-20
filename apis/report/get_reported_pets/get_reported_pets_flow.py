from flask import jsonify
from models.pet import Pet


class GetReportedPetsFlow:

    def __call__(self, request):

        owner_id = request.args["owner_id"]

        pets_list = Pet.objects(
            owner_id=owner_id,
            is_reported=True
            
        )
        
        pets_jsons_list = []
        pets_jsons_list = list(map(lambda pet_obj: pet_obj.to_json(), pets_list))

        return jsonify({"pets": pets_jsons_list})


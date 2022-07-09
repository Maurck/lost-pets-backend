from models.pet import Pet
from utils.utils import json_message, json_message_error_code 


class DeletePetFlow:

    def __call__(self, request):
        pet_id = request.args.get('id')    
        pet = Pet.objects(
            id=pet_id
        ).first()

        if pet is None:
            return json_message_error_code("Mascota no encontrada")

        pet.delete()

        return json_message("Mascota Borrada")

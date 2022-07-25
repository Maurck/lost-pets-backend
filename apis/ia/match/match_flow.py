from models.user import User
from models.pet import Pet
from utils.utils import json_message, json_message_error_code 


class MatchFlow:

    def __call__(self, request):
        user_id = request.args.get('id')    
        user = User.objects(
            id=user_id
        ).first()

        if user is None:
            return json_message_error_code("Usuario no encontrado")

        user_pets = Pet.objects(
            owner_id=user_id
        )

        if user_pets is not None:
            user_pets.delete()
        
        user.delete()

        return json_message("Usuario borrado")

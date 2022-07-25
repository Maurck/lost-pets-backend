from flask import jsonify
from models.user import User
from models.pet import Pet
from utils.utils import json_message


class DeleteUsersFlow:

    def __call__(self):
        User.objects.delete()
        Pet.objects.delete()
        
        return json_message("Usuarios borrados")

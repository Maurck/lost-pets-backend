from flask import jsonify
from models.pet import Pet
from utils.utils import json_message


class DeletePetsFlow:

    def __call__(self):
        Pet.objects.delete()
        return json_message("Mascotas borradas")

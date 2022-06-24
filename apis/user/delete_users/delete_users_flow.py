from flask import jsonify
from models.user import User
from utils.utils import json_message


class DeleteUsersFlow:

    def __call__(self):
        User.objects.delete()
        return json_message("Usuarios borrados")

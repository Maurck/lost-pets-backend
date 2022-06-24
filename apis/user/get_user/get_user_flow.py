from flask import jsonify
from models.user import User
from utils.utils import json_message


class GetUserFlow:
    def __call__(self, request):

        user_id = request.args.get('id')

        user_obj = User.objects(
            id=user_id
        ).first()

        if user_obj is not None:
            return jsonify({"user": user_obj.to_json()})

        return json_message("Usuario no encontrado")

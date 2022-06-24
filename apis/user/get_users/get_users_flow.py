from flask import jsonify
from models.user import User


class GetUsersFlow:

    def __call__(self):
        users_list = User.objects()
        users_jsons_list = []
        users_jsons_list = list(map(lambda user_obj: user_obj.to_json(), users_list))

        return jsonify({"users": users_jsons_list})


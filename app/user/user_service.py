# import uuid
# import datetime

# from app.main import db
# from app.main.model.user import User

from .model.user import User

from .user_repository import save


def save_new_user(body):

    new_user = save(body)
    # user = User.query.filter_by(email=data['email']).first()
    # if not user:
    #     new_user = User(
    #         public_id=str(uuid.uuid4()),
    #         email=data['email'],
    #         username=data['username'],
    #         password=data['password'],
    #         registered_on=datetime.datetime.utcnow()
    #     )
    #     save_changes(new_user)
    #     response_object = {
    #         'status': 'success',
    #         'message': 'Successfully registered.'
    #     }
    #     return response_object, 201
    # else:
    #     response_object = {
    #         'status': 'fail',
    #         'message': 'User already exists. Please Log in.',
    #     }
    #     return response_object, 409
    return {
        'msg': 'usario guardado',
        'user': new_user
    }, 201


def get_all_users():
    users_list = User.objects()
    users_jsons_list = []
    users_jsons_list = list(map(lambda user_obj: user_obj.to_json(), users_list))

    # return User.query.all()
    return users_jsons_list


def get_a_user(public_id):
    # return User.query.filter_by(public_id=public_id).first()
    return {
        'name': 'Mauricio'
    }


# def save_changes(data):
#     db.session.add(data)
#     db.session.commit()
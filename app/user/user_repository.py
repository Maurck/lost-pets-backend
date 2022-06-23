
from .model.user import User

def save(body):
    new_user = User(
        name=body['name'],
        mother_lastname=body['mother_lastname'],
        father_lastname=body['father_lastname'],
        address=body['address'],
        dni=body['dni'],
        email=body['email'],
        phone_number=body['phone_number'],
        nickname=body['nickname']
    )

    new_user.save()

    return new_user.to_json()

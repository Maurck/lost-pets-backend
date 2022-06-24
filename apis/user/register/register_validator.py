from utils.utils import validate_parameters

register_body_schema = {
    'name': {
        'nullable': False,
        'required': True
    },
    'password': {
        'nullable': False,
        'required': True
    },
    'email': {
        'nullable': False,
        'required': True,
        # 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    },    
    'mother_lastname': {
        'nullable': False,
        'required': True
    },
    'father_lastname': {
        'nullable': False,
        'required': True
    },
    'address': {
        'nullable': False,
        'required': True
    },
    'dni': {
        'nullable': False,
        'required': True
    },
    'phone_number': {
        'nullable': False,
        'required': True
    },
    'nickname': {
        'nullable': False,
        'required': True
    }
}

class RegisterValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.json, register_body_schema)
        return body_validation_errors
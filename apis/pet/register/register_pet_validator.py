from utils.utils import validate_parameters

register_pet_body_schema = {
    'name': {
        'nullable': False,
        'required': True
    },
    'gender': {
        'nullable': False,
        'required': True
    },
    'birthdate': {
        'type': 'date',
        'nullable': False,
        'required': True
    },    
    'color': {
        'nullable': False,
        'required': True
    },
    'breed': {
        'nullable': False,
        'required': True
    },
    'characteristics': {
        'nullable': False,
        'required': True
    },
    'size': {
        'nullable': False,
        'required': True
    },
    'owner_id': {
        'type': 'string',
        'nullable': False,
        'required': True,
        'minlength': 24,
        'maxlength': 24
    }
}

class RegisterPetValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.json, register_pet_body_schema)
        return body_validation_errors
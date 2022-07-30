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
    },
    'img': {
        'required': True,
        'nullable': False
    }
}

class RegisterPetValidator:

    def __call__(self, request):

        full_request = dict(request.form.copy(), **request.files.copy())

        body_validation_errors = validate_parameters(full_request, register_pet_body_schema)
        return body_validation_errors
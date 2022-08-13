from utils.utils import validate_parameters

report_pet_body_schema = {
    'address': {
        'nullable': False,
        'required': True
    },
    'description': {
        'nullable': False,
        'required': True
    },
    'pet_id': {
        'type': 'string',
        'nullable': False,
        'required': True,
        'minlength': 24,
        'maxlength': 24
    },    
    'reporter_id': {
        'type': 'string',
        'nullable': False,
        'required': True,
        'minlength': 24,
        'maxlength': 24
    },
    'reported_img': {
        'nullable': False,
        'required': True
    }
}

class ReportPetValidator:

    def __call__(self, request):

        full_request = dict(request.form.copy(), **request.files.copy())

        body_validation_errors = validate_parameters(full_request, report_pet_body_schema)
        return body_validation_errors
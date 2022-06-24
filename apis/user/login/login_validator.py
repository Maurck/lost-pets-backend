from utils.utils import validate_parameters

login_body_schema = {
    'password': {
        'nullable': False,
        'required': True
    },
    'email': {
        'nullable': False,
        'required': True
    } 
}

class LoginValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.json, login_body_schema)
        return body_validation_errors
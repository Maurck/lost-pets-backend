from utils.utils import validate_parameters

get_pet_query_schema = {
    'id': {
        'type': 'string',
        'nullable': False,
        'required': True,
        'minlength': 24,
        'maxlength': 24
    }
}

class GetPetValidator:

    def __call__(self, request):
        query_validation_errors = validate_parameters(request.args, get_pet_query_schema)
        return query_validation_errors
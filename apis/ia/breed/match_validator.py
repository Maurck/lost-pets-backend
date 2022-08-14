from utils.utils import validate_parameters

match_query_schema = {
        'reference': {
            'type': 'string'
        },
        'img_from_user': {
        }
}

class MatchValidation:

    def __call__(self, request):
        
        query_validation_errors = validate_parameters(request.form.copy(), match_query_schema)
        return query_validation_errors


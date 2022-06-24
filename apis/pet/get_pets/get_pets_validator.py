from utils.utils import validate_parameters

get_pets_query_schema = {
}

class GetPetsValidation:

    def __call__(self, request):
        
        query_validation_errors = validate_parameters(request.args.copy(), get_pets_query_schema)
        return query_validation_errors


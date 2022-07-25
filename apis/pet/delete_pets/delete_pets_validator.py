from utils.utils import validate_parameters

delete_pets_query_schema = {
}

class DeletePetsValidation:

    def __call__(self, request):
        
        query_validation_errors = validate_parameters(request.args.copy(), delete_pets_query_schema)
        return query_validation_errors


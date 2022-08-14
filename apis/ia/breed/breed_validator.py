from utils.utils import validate_parameters

breed_query_schema = {
        'pet_image': {
        }
}

class BreedValidation:

    def __call__(self, request):
        
        query_validation_errors = validate_parameters(request.form.copy(), breed_query_schema)
        return query_validation_errors


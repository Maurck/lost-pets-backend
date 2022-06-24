from utils.utils import validate_parameters

get_users_query_schema = {
}

class GetUsersValidation:

    def __call__(self, request):
        
        query_validation_errors = validate_parameters(request.args.copy(), get_users_query_schema)
        return query_validation_errors


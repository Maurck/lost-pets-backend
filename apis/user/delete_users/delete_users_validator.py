from utils.utils import validate_parameters

delete_users_query_schema = {
}

class DeleteUsersValidation:

    def __call__(self, request):
        
        query_validation_errors = validate_parameters(request.args.copy(), delete_users_query_schema)
        return query_validation_errors


from .delete_users_validator import DeleteUsersValidation
from .delete_users_flow import DeleteUsersFlow


class DeleteUsers:

    def __call__(self, request):

        delete_users_validation = DeleteUsersValidation()
        delete_users_validation_errors = delete_users_validation(request)
        if delete_users_validation_errors:
            return delete_users_validation_errors

        delete_users_flow = DeleteUsersFlow()
        return delete_users_flow()

            

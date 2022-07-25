from .delete_user_validator import DeleteUserValidation
from .delete_user_flow import DeleteUserFlow


class DeleteUser:

    def __call__(self, request):

        delete_user_validation = DeleteUserValidation()
        delete_user_validation_errors = delete_user_validation(request)
        if delete_user_validation_errors:
            return delete_user_validation_errors

        delete_user_flow = DeleteUserFlow()
        return delete_user_flow(request)

            

from .delete_pets_validator import DeletePetsValidation
from .delete_pets_flow import DeletePetsFlow


class DeletePets:

    def __call__(self, request):

        delete_pets_validation = DeletePetsValidation()
        delete_pets_validation_errors = delete_pets_validation(request)
        if delete_pets_validation_errors:
            return delete_pets_validation_errors

        delete_pets_flow = DeletePetsFlow()
        return delete_pets_flow()

            

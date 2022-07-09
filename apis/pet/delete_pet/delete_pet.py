from .delete_pet_validator import DeletePetValidation
from .delete_pet_flow import DeletePetFlow


class DeletePet:

    def __call__(self, request):

        delete_pet_validation = DeletePetValidation()
        delete_pet_validation_errors = delete_pet_validation(request)
        if delete_pet_validation_errors:
            return delete_pet_validation_errors

        delete_pet_flow = DeletePetFlow()
        return delete_pet_flow(request)

            

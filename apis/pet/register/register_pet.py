from .register_pet_validator import RegisterPetValidator
from .register_pet_flow import RegisterPetFlow


class RegisterPet:

    def __call__(self, request):

        register_pet_validation = RegisterPetValidator()
        register_pet_validation_errors = register_pet_validation(request)
        if register_pet_validation_errors:
            return register_pet_validation_errors

        register_pet_flow = RegisterPetFlow()
        return register_pet_flow(request)

            

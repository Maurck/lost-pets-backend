from .get_pet_validator import GetPetValidator
from .get_pet_flow import GetPetFlow


class GetPet:

    def __call__(self, request):

        get_pet_validation = GetPetValidator()
        get_pet_validation_errors = get_pet_validation(request)
        if get_pet_validation_errors:
            return get_pet_validation_errors

        get_pet_flow = GetPetFlow()
        return get_pet_flow(request)

            

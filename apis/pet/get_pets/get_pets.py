from .get_pets_validator import GetPetsValidation
from .get_pets_flow import GetPetsFlow


class GetPets:

    def __call__(self, request):

        get_pets_validation = GetPetsValidation()
        get_pets_validation_errors = get_pets_validation(request)
        if get_pets_validation_errors:
            return get_pets_validation_errors

        get_pets_flow = GetPetsFlow()
        return get_pets_flow()

            

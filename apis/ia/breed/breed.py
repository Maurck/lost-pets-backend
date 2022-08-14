from .breed_validator import BreedValidation
from .breed_flow import BreedFlow


class Breed:

    def __call__(self, request):

        breed_validation = BreedValidation()
        breed_validation_errors = breed_validation(request)
        if breed_validation_errors:
            return breed_validation_errors

        breed_flow = BreedFlow()
        return breed_flow(request)

            

from .get_reported_pets_validator import GetReportedPetsValidation
from .get_reported_pets_flow import GetReportedPetsFlow


class GetReportedPets:

    def __call__(self, request):

        get_reported_pets_validation = GetReportedPetsValidation()
        get_reported_pets_validation_errors = get_reported_pets_validation(request)
        if get_reported_pets_validation_errors:
            return get_reported_pets_validation_errors

        get_reported_pets_flow = GetReportedPetsFlow()
        return get_reported_pets_flow(request)

            

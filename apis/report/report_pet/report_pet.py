from .report_pet_validator import ReportPetValidator
from .report_pet_flow import ReportPetFlow


class ReportPet:

    def __call__(self, request):

        report_pet_validation = ReportPetValidator()
        report_pet_validation_errors = report_pet_validation(request)
        if report_pet_validation_errors:
            return report_pet_validation_errors

        report_pet_flow = ReportPetFlow()
        return report_pet_flow(request)

            

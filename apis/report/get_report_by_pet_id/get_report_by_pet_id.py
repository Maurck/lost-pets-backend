from .get_report_by_pet_id_validator import GetReportByPetIdValidator
from .get_report_by_pet_id_flow import GetReportByPetIdFlow


class GetReportByPetId:

    def __call__(self, request):

        get_report_by_pet_id_validation = GetReportByPetIdValidator()
        get_report_by_pet_id_validation_errors = get_report_by_pet_id_validation(request)
        if get_report_by_pet_id_validation_errors:
            return get_report_by_pet_id_validation_errors

        get_report_by_pet_id_flow = GetReportByPetIdFlow()
        return get_report_by_pet_id_flow(request)

            

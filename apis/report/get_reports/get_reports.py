from .get_reports_validator import GetReportsValidation
from .get_reports_flow import GetReportsFlow


class GetReports:

    def __call__(self, request):

        get_reports_validation = GetReportsValidation()
        get_reports_validation_errors = get_reports_validation(request)
        if get_reports_validation_errors:
            return get_reports_validation_errors

        get_reports_flow = GetReportsFlow()
        return get_reports_flow()

            

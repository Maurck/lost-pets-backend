from .delete_report_validator import DeleteReportValidation
from .delete_report_flow import DeleteReportFlow


class DeleteReport:

    def __call__(self, request):

        delete_report_validation = DeleteReportValidation()
        delete_report_validation_errors = delete_report_validation(request)
        if delete_report_validation_errors:
            return delete_report_validation_errors

        delete_report_flow = DeleteReportFlow()
        return delete_report_flow(request)

            

from utils.utils import validate_parameters

delete_report_query_schema = {
        'id': {
        'type': 'string',
        'nullable': False,
        'required': True,
        'minlength': 24,
        'maxlength': 24
    }
}

class DeleteReportValidation:

    def __call__(self, request):
        
        query_validation_errors = validate_parameters(request.args.copy(), delete_report_query_schema)
        return query_validation_errors


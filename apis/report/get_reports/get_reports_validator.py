from utils.utils import validate_parameters

get_reports_query_schema = {
}

class GetReportsValidation:

    def __call__(self, request):
        
        query_validation_errors = validate_parameters(request.args.copy(), get_reports_query_schema)
        return query_validation_errors


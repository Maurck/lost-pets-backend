from utils.utils import validate_parameters

get_reported_pets_query_schema = {
    "owner_id": {
        "type": "string",
        "required": True,
        "nullable": False
    }
}

class GetReportedPetsValidation:

    def __call__(self, request):
        
        query_validation_errors = validate_parameters(request.args.copy(), get_reported_pets_query_schema)
        return query_validation_errors


from utils.utils import validate_parameters

get_pets_by_owner_id_query_schema = {
    "owner_id": {
        "type": "string",
        "required": True,
        "nullable": False
    }
}

class GetPetsByOwnerIdValidation:

    def __call__(self, request):
        
        query_validation_errors = validate_parameters(request.args.copy(), get_pets_by_owner_id_query_schema)
        return query_validation_errors


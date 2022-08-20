from utils.utils import validate_parameters

get_report_by_pet_id_query_schema = {
    'pet_id': {
        'type': 'string',
        'nullable': False,
        'required': True,
        'minlength': 24,
        'maxlength': 24
    }
}

class GetReportByPetIdValidator:

    def __call__(self, request):
        query_validation_errors = validate_parameters(request.args, get_report_by_pet_id_query_schema)
        return query_validation_errors
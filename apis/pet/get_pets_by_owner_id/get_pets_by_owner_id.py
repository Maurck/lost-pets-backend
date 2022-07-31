from .get_pets_by_owner_id_validator import GetPetsByOwnerIdValidation
from .get_pets_by_owner_id_flow import GetPetsByOwnerIdFlow


class GetPetsByOwnerId:

    def __call__(self, request):

        get_pets_by_owner_id_validation = GetPetsByOwnerIdValidation()
        get_pets_by_owner_id_validation_errors = get_pets_by_owner_id_validation(request)
        if get_pets_by_owner_id_validation_errors:
            return get_pets_by_owner_id_validation_errors

        get_pets_by_owner_id_flow = GetPetsByOwnerIdFlow()
        return get_pets_by_owner_id_flow(request)

            

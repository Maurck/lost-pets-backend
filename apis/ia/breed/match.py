from .match_validator import MatchValidation
from .match_flow import MatchFlow


class Match:

    def __call__(self, request):

        match_validation = MatchValidation()
        match_validation_errors = match_validation(request)
        if match_validation_errors:
            return match_validation_errors

        match_flow = MatchFlow()
        return match_flow(request)

            

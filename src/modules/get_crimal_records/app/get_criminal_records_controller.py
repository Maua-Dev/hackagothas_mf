from src.modules.get_crimal_records.app.get_criminal_records_usecase import GetCriminalRecordsUseCase
from src.modules.get_crimal_records.app.get_criminal_records_viewmodel import GetCriminalRecordsViewmodel
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.errors.domain_errors import EntityError

class GetCriminalRecordsController:
    def __init__(self, get_criminal_records_use_case: GetCriminalRecordsUseCase):
        self.get_criminal_records_use_case = get_criminal_records_use_case

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.data.get("criminal_records_id") == None:
                return MissingParameters("Missing criminal_records_id")
        
            
            criminal_records_response = self.get_criminal_records_use_case(request.data.get("criminal_records_id"))
            viewmodel = GetCriminalRecordsViewmodel(criminal_records_response)
            
            return OK(body=viewmodel.to_dict())
            
        except EntityError as err:
            return BadRequest(body=err.message)
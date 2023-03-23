from http.client import HTTPResponse
from src.modules.get_crimal_records.app.get_criminal_records_usecase import GetCriminalRecordsUseCase
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.external_interfaces.http_codes import HttpRequest, HttpResponse, BadRequest
from src.shared.helpers.errors.controller_errors import MissingParameters, EntityError

class GetCriminalRecordsController:
    def __init__(self, get_criminal_records_use_case: GetCriminalRecordsUseCase):
        self.get_criminal_records_use_case = get_criminal_records_use_case

    def __call__(self, request: HttpRequest) -> HTTPResponse:
        try:
            if request.data.get("criminal_records_id") == None:
                return MissingParameters("Missing criminal_records_id")
            if request.data.get("name") == None:
                return MissingParameters("Missing name")
            if request.data.get("common_attack_region") == None:
                return MissingParameters("Missing common_attack_region")
            if request.data.get("description") == None:
                return MissingParameters("Missing description")
            if request.data.get("gender") == None:
                return MissingParameters("Missing gender")
            if request.data.get("crime_type") == None:
                return MissingParameters("Missing crime_type")
            if request.data.get("arrested") == None:
                return MissingParameters("Missing arrested")
            
            if type(request.data.get("gender") != str):
                raise EntityError("gender")
            gender_values = [val.value for val in GENDER]
            if request.data.get("gender") not in gender_values:
                raise EntityError("gender")
            
            criminal = Criminal(name=request.data.get("name"), common_attack_region=request.data.get("common_attack_region"),
            description=request.data.get("description"))
            
        except EntityError as err:
            return BadRequest(body=err.message)
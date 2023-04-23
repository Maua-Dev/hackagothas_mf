from hackagothas_mf.src.modules.create_criminal_records.app.create_criminal_records_usecase import CreateCriminalRecordsUseCase
from hackagothas_mf.src.shared.helpers.errors.controller_errors import MissingParameters
from hackagothas_mf.src.shared.helpers.errors.domain_errors import EntityError
from hackagothas_mf.src.shared.helpers.errors.usecase_errors import ForbiddenAction
from hackagothas_mf.src.shared.helpers.external_interfaces.http_codes import BadRequest, InternalServerError, NotFound
from hackagothas_mf.src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


class CreateCriminalRecordsController:
    def __init__(self,usecase: CreateCriminalRecordsUseCase):
        self.CreateCriminalRecordsUseCase = usecase
    
    def __call__(self,request: HttpRequest) -> HttpResponse:
        try:
            if request.data.get('criminal_records_id') == None:
                raise MissingParameters ('criminal_records_id') 
            if request.data.get('name') == None:
                raise MissingParameters ('name') 
            if request.data.get('description') == None:
                raise MissingParameters ('description') 
            if request.data.get('gender') == None:
                raise MissingParameters ('gender') 
            if request.data.get('common_attack_region') == None:
                raise MissingParameters ('common_attack_region') 
            if request.data.get('crime_type') == None:
                raise MissingParameters ('crime_type') 
            if request.data.get('arrested') == None:
                raise MissingParameters ('arrested')
            if request.data.get('crime_id') == None:
                raise MissingParameters ('crime_id')

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except ForbiddenAction as err:
            return NotFound(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])
            
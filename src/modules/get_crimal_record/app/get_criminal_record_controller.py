
from src.modules.get_crimal_record.app.get_criminal_record_usecase import GetCriminalRecordUseCase
from src.modules.get_crimal_record.app.get_criminal_record_viewmodel import GetCriminalRecordViewmodel
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.errors.domain_errors import EntityError

class GetCriminalRecordController:
    def __init__(self, get_criminal_record_use_case: GetCriminalRecordUseCase):
        self.get_criminal_record_use_case = get_criminal_record_use_case

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.data.get("criminal_record_id") == None:
                return MissingParameters("criminal_record_id")
        
            
            criminal_record_response = self.get_criminal_record_use_case(request.data.get("criminal_record_id"))
            viewmodel = GetCriminalRecordViewmodel(criminal_record_response)
            
            return OK(body=viewmodel.to_dict())
            
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
        
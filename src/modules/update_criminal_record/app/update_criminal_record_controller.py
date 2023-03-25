from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUseCase
from src.modules.update_criminal_record.app.update_criminal_record_viewmodel import UpdateCriminalRecordViewModel
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse

class UpdateCriminalRecordController:
    usecase: UpdateCriminalRecordUseCase
    
    def __init__(self, usecase: UpdateCriminalRecordUseCase) -> None:
        self.usecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.data.get("criminal_record_id") == None:
                raise MissingParameters("criminal_record_id")
            if request.data.get("new_name") == None:
                raise MissingParameters("new_name")
            
            updated_criminal_record = self.usecase(
                criminal_record_id=request.data.get("criminal_record_id"),
                new_name=request.data.get("new_name"),
                new_gender=request.data.get("new_gender"),
                new_common_attack_region=request.data.get("new_common_attack_region"),
                new_description=request.data.get("new_description"),
                new_arrested=request.data.get("new_arrested"),
                new_crime_type=request.data.get("new_crime_type")
            )
            
            viewmodel = UpdateCriminalRecordViewModel(updated_criminal_record)
            
            return OK(viewmodel.to_dict())
        
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
        
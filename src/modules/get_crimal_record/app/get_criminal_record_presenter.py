from src.modules.get_crimal_record.app.get_criminal_record_controller import GetCriminalRecordController
from src.modules.get_crimal_record.app.get_criminal_record_usecase import GetCriminalRecordUseCase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse

from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock

def get_criminal_record_presenter(event, context):
    repo = CriminalRecordRepositoryMock()
    usecase = GetCriminalRecordUseCase(repo)
    controller = GetCriminalRecordController(usecase)
    
    http_request = FastAPIHttpRequest(data=event)
    response = controller(http_request)
    http_response = FastAPIHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
    return http_response.to_dict()
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from .get_criminal_records_controller import GetCriminalRecordsController
from .get_criminal_records_usecase import GetCriminalRecordsUseCase
from src.shared.infra.repositories.criminal_records_repository_mock import CriminalRecordsRepositoryMock

def get_criminal_records_presenter(event, context):
    repo = CriminalRecordsRepositoryMock()
    usecase = GetCriminalRecordsUseCase(repo)
    controller = GetCriminalRecordsController(usecase)
    
    http_request = FastAPIHttpRequest(data=event)
    response = controller(http_request)
    http_response = FastAPIHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
    return http_response.to_dict()
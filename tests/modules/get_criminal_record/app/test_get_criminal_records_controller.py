from src.modules.get_crimal_record.app.get_criminal_record_controller import GetCriminalRecordController
from src.modules.get_crimal_record.app.get_criminal_record_usecase import GetCriminalRecordUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCriminalRecordController:
    def test_get_criminal_record_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUseCase(repo)
        controller = GetCriminalRecordController(usecase)
        
        
        body = {
            "criminal_record_id": "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        }
        request = HttpRequest(body=body)
        
        response = controller(request=request)
        
        
        assert response.status_code == 200
        assert response.body["message"] == "CriminalRecord was retrieved"
        assert response.body["criminal_record"]["criminal_record_id"] == "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        assert response.body["criminal_record"]["criminal"]["name"] == "Digao"
        assert response.body["criminal_record"]["criminal"]["common_attack_region"] == "Santo Andre"
        assert response.body["criminal_record"]["criminal"]["description"] == "Digao gosta de roubar"
        assert response.body["criminal_record"]["criminal"]["gender"] == "MALE"
        assert response.body["criminal_record"]["crime_type"] == "ROBBERY"
        assert response.body["criminal_record"]["arrested"] == True
    
    def test_get_criminal_record_controller_with_invalid_criminal_record_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUseCase(repo)
        controller = GetCriminalRecordController(usecase)
        
        
        body = {
            "criminal_record_id": "invalid_id"
        }
        request = HttpRequest(body=body)
        
        response = controller(request=request)
        
        
        assert response.status_code == 400
        assert response.body == "Field criminal_record_id is not valid"
    
    def test_get_criminal_record_controller_without_criminal_record_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUseCase(repo)
        controller = GetCriminalRecordController(usecase)
        
        
        body = {
            "criminal_record_id": ""
        }
        request = HttpRequest(body=body)
        
        response = controller(request=request)
        
        
        assert response.status_code == 400
        assert response.body == "Field criminal_record_id is not valid"
        
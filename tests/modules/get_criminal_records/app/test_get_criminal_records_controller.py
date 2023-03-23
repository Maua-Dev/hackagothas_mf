from src.modules.get_crimal_records.app.get_criminal_records_controller import GetCriminalRecordsController
from src.modules.get_crimal_records.app.get_criminal_records_usecase import GetCriminalRecordsUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_records_repository_mock import CriminalRecordsRepositoryMock


class Test_GetCriminalRecordsController:
    def test_get_criminal_records_controller(self):
        repo = CriminalRecordsRepositoryMock()
        usecase = GetCriminalRecordsUseCase(repo)
        controller = GetCriminalRecordsController(usecase)
        
        
        body = {
            "criminal_records_id": "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        }
        request = HttpRequest(body=body)
        
        response = controller(request=request)
        
        
        assert response.status_code == 200
        assert response.body["message"] == "CriminalRecord was retrieved"
        assert response.body["criminal_records"]["criminal_records_id"] == "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        assert response.body["criminal_records"]["criminal"]["name"] == "Digao"
        assert response.body["criminal_records"]["criminal"]["common_attack_region"] == "Santo Andre"
        assert response.body["criminal_records"]["criminal"]["description"] == "Digao gosta de roubar"
        assert response.body["criminal_records"]["criminal"]["gender"] == "MALE"
        assert response.body["criminal_records"]["crime_type"] == "ROBBERY"
        assert response.body["criminal_records"]["arrested"] == True
    
    def test_get_criminal_records_controller_with_invalid_criminal_records_id(self):
        repo = CriminalRecordsRepositoryMock()
        usecase = GetCriminalRecordsUseCase(repo)
        controller = GetCriminalRecordsController(usecase)
        
        
        body = {
            "criminal_records_id": "invalid_id"
        }
        request = HttpRequest(body=body)
        
        response = controller(request=request)
        
        
        assert response.status_code == 400
        assert response.body == "Field criminal_records_id is not valid"
    
    def test_get_criminal_records_controller_without_criminal_records_id(self):
        repo = CriminalRecordsRepositoryMock()
        usecase = GetCriminalRecordsUseCase(repo)
        controller = GetCriminalRecordsController(usecase)
        
        
        body = {
            "criminal_records_id": ""
        }
        request = HttpRequest(body=body)
        
        response = controller(request=request)
        
        
        assert response.status_code == 400
        assert response.body == "Field criminal_records_id is not valid"
        
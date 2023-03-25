import pytest
from src.modules.update_criminal_record.app.update_criminal_record_controller import UpdateCriminalRecordController
from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUseCase
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_UpdateCriminalRecordController:
    def test_update_criminal_record_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUseCase(repo)
        controller = UpdateCriminalRecordController(usecase)
        
        request = HttpRequest(body={
            "criminal_record_id": "e5a328bb-8522-4530-aa5a-c879a2d87bf3",
            "new_name": "Rodrigo",
            "new_common_attack_region": "Sao Paulo",
            "new_description": "Rodrigo gosta de traficar",
            "new_gender": GENDER.OTHER,
            "new_crime_type": CRIME_TYPE.DRUG_TRAFFICKING,
            "new_arrested": False
        })
        
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body["message"] == "CriminalRecord was updated"
        assert response.body["criminal_record"]["criminal_record_id"] == "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        assert response.body["criminal_record"]["criminal"]["name"] == "Rodrigo"
        assert response.body["criminal_record"]["criminal"]["common_attack_region"] == "Sao Paulo"
        assert response.body["criminal_record"]["criminal"]["description"] == "Rodrigo gosta de traficar"
        assert response.body["criminal_record"]["criminal"]["gender"] == "OTHER"
        assert response.body["criminal_record"]["crime_type"] == "DRUG_TRAFFICKING"
        assert response.body["criminal_record"]["arrested"] == False
        
    def test_update_criminal_record_controller_missing_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUseCase(repo)
        controller = UpdateCriminalRecordController(usecase)
        
        request = HttpRequest(body={
            "new_name": "Rodrigo",
            "new_common_attack_region": "Sao Paulo",
            "new_description": "Rodrigo gosta de traficar",
            "new_gender": GENDER.OTHER,
            "new_crime_type": CRIME_TYPE.DRUG_TRAFFICKING,
            "new_arrested": False
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field criminal_record_id is missing"
    
    def test_update_criminal_record_controller_missing_name(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUseCase(repo)
        controller = UpdateCriminalRecordController(usecase)
        
        request = HttpRequest(body={
            "criminal_record_id": "e5a328bb-8522-4530-aa5a-c879a2d87bf3",
            "new_common_attack_region": "Sao Paulo",
            "new_description": "Rodrigo gosta de traficar",
            "new_gender": GENDER.OTHER,
            "new_crime_type": CRIME_TYPE.DRUG_TRAFFICKING,
            "new_arrested": False
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field new_name is missing"
    
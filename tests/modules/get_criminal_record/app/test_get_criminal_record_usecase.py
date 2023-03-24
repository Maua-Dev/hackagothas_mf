import pytest
from src.modules.get_crimal_record.app.get_criminal_record_usecase import GetCriminalRecordUseCase
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCriminalRecordUseCase:
    def test_get_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUseCase(repo)
        criminal_record_response = usecase("e5a328bb-8522-4530-aa5a-c879a2d87bf3")
        
        assert criminal_record_response.criminal_record_id == "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        assert criminal_record_response.criminal.name == "Digao"
        assert criminal_record_response.criminal.common_attack_region == "Santo Andre"
        assert criminal_record_response.criminal.description == "Digao gosta de roubar"
        assert criminal_record_response.criminal.gender == GENDER.MALE
        assert criminal_record_response.arrested == True
        assert criminal_record_response.crime_type == CRIME_TYPE.ROBBERY
        
    def test_get_criminal_record_not_found(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUseCase(repo)
        
        with pytest.raises(EntityError):
            criminal_record_response = usecase("macaco")
            
        
    def test_get_criminal_record_invalid_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUseCase(repo)
        
        with pytest.raises(EntityError):
            criminal_record_response = usecase(1)  
    
    def test_get_criminal_record_without_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUseCase(repo)
        
        with pytest.raises(EntityError):
            criminal_record_response = usecase("")


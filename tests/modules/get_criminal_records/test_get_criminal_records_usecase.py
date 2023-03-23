import pytest
from src.modules.get_crimal_records.app.get_criminal_records_usecase import GetCriminalRecordsUseCase
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_records_repository_mock import CriminalRecordsRepositoryMock


class Test_GetCriminalRecordsUseCase:
    def test_get_criminal_records(self):
        repo = CriminalRecordsRepositoryMock()
        usecase = GetCriminalRecordsUseCase(repo)
        criminal_record_response = usecase("e5a328bb-8522-4530-aa5a-c879a2d87bf3")
        
        assert criminal_record_response.criminal_records_id == "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        assert criminal_record_response.criminal.name == "Digão"
        assert criminal_record_response.criminal.common_attack_region == "Santo André"
        assert criminal_record_response.criminal.description == "Digão gosta de roubar"
        assert criminal_record_response.criminal.gender == GENDER.MALE
        assert criminal_record_response.arrested == True
        assert criminal_record_response.crime_type == CRIME_TYPE.ROBBERY
        
    def test_get_criminal_records_not_found(self):
        repo = CriminalRecordsRepositoryMock()
        usecase = GetCriminalRecordsUseCase(repo)
        
        with pytest.raises(NoItemsFound):
            criminal_record_response = usecase("macaco")
            
        
    def test_get_criminal_records_invalid_id(self):
        repo = CriminalRecordsRepositoryMock()
        usecase = GetCriminalRecordsUseCase(repo)
        
        with pytest.raises(EntityError):
            criminal_record_response = usecase(1)        


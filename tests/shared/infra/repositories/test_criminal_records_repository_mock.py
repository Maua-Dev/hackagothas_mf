import pytest
from typing import List
from src.shared.domain.entities.criminal_records import CriminalRecords
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.errors.domain_errors import EntityError

from src.shared.infra.repositories.criminal_records_repository_mock import CriminalRecordsRepositoryMock

class Test_CriminalRecordsRepositoryMock():
    def test_get_criminal_records(self):
        repo = CriminalRecordsRepositoryMock()
        repo_response = repo.get_criminal_records(criminal_records_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3")
        
        assert type(repo_response) == CriminalRecords
        assert repo_response.criminal_records_id == "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        assert repo_response.criminal.name == "Digao"
        assert repo_response.criminal.common_attack_region == "Santo Andre"
        assert repo_response.criminal.description == "Digao gosta de roubar"
        assert repo_response.criminal.gender == GENDER.MALE
        assert repo_response.arrested == True
        assert repo_response.crime_type == CRIME_TYPE.ROBBERY
    
    def test_get_criminal_records_not_found(self):
        repo = CriminalRecordsRepositoryMock()
        repo_response = repo.get_criminal_records(criminal_records_id="macaco")
        
        assert repo_response == None 

    def test_create_criminal_records(self):
        repo = CriminalRecordsRepositoryMock
        lenght_bef = len(repo.criminal_records)
        repo.create_criminal_records(CriminalRecords(
            criminal_records_id="4b276259-43d6-44f6-917b-e3091b88034X",
            arrested=True,
            crime_type=CRIME_TYPE.MURDER,
            criminal=repo.criminal[3]) )
        lenght_aft = len(repo.criminal_records)

        assert lenght_aft == lenght_bef+1
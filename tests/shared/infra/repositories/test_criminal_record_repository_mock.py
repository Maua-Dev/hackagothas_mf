import pytest
from typing import List
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.errors.domain_errors import EntityError

from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock

class Test_CriminalRecordRepositoryMock():
    def test_get_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        repo_response = repo.get_criminal_record(criminal_record_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3")
        
        assert type(repo_response) == CriminalRecord
        assert repo_response.criminal_record_id == "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        assert repo_response.criminal.name == "Digao"
        assert repo_response.criminal.common_attack_region == "Santo Andre"
        assert repo_response.criminal.description == "Digao gosta de roubar"
        assert repo_response.criminal.gender == GENDER.MALE
        assert repo_response.arrested == True
        assert repo_response.crime_type == CRIME_TYPE.ROBBERY
    
    def test_get_criminal_record_not_found(self):
        repo = CriminalRecordRepositoryMock()
        repo_response = repo.get_criminal_record(criminal_record_id="macaco")
        
        assert repo_response == None 
        
    def test_update_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        repo_response = repo.update_criminal_record(
            criminal_record_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3",
            new_arrested=False,
            new_common_attack_region="Sao Paulo",
            new_crime_type=CRIME_TYPE.DRUG_TRAFFICKING,
            new_description="Rodrigo gosta de traficar",
            new_gender=GENDER.OTHER,
            new_name="Rodrigo"
        )
        
        assert type(repo_response) == CriminalRecord
        assert repo_response.criminal_record_id == "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        assert repo_response.criminal.name == "Rodrigo"
        assert repo_response.criminal.common_attack_region == "Sao Paulo"
        assert repo_response.criminal.description == "Rodrigo gosta de traficar"
        assert repo_response.criminal.gender == GENDER.OTHER
        assert repo_response.arrested == False
        assert repo_response.crime_type == CRIME_TYPE.DRUG_TRAFFICKING
    
    def test_update_criminal_record_one_item(self):
        repo = CriminalRecordRepositoryMock()
        repo_response = repo.update_criminal_record(
            criminal_record_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3",
            new_name="Rodrigo Siqueira"
        )
        
        assert type(repo_response) == CriminalRecord
        assert repo_response.criminal_record_id == "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        assert repo_response.criminal.name == "Rodrigo Siqueira"
        assert repo_response.criminal.common_attack_region == "Santo Andre"
        assert repo_response.criminal.description == "Digao gosta de roubar"
        assert repo_response.criminal.gender == GENDER.MALE
        assert repo_response.arrested == True
        assert repo_response.crime_type == CRIME_TYPE.ROBBERY
    
    def test_update_criminal_record_not_found(self):
        repo = CriminalRecordRepositoryMock()
        repo_response = repo.update_criminal_record(
            criminal_record_id="macaco",
        )
        
        assert repo_response == None
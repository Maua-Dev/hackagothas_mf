from hackagothas_mf.src.shared.domain.enums.criminal_type import CRIME_TYPE
import pytest
from src.shared.domain.entities.criminal_records import CriminalRecords

from src.shared.infra.repositories.criminal_records_repository_mock import CriminalRecordsRepositoryMock

class Test_CriminalRecordsRepositoryMock():
    def test_get_criminal_records_repository_mock(self):
        repo = CriminalRecordsRepositoryMock()
        repo_response = repo.get_criminal_records(criminal_records_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3")
        
        assert type(repo_response) == list

    def test_create_criminal_records(self):
        repo = CriminalRecordsRepositoryMock()
        lenght_bef = len(repo.criminal_records)
        repo.create_criminal_records(CriminalRecords(
            criminal_records_id="4b276259-43d6-44f6-917b-e3091b88034X",
            arrested=True,
            crime_type=CRIME_TYPE.MURDER,
            criminal=repo.criminal[3]) )
        lenght_aft = len(repo.criminal_records)

        assert lenght_aft == lenght_bef+1
        
        
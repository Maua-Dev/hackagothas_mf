import pytest
from src.shared.domain.entities.criminal_records import CriminalRecords

from src.shared.infra.repositories.criminal_records_repository_mock import CriminalRecordsRepositoryMock

class Test_CriminalRecordsRepositoryMock():
    def test_get_criminal_records_repository_mock(self):
        repo = CriminalRecordsRepositoryMock()
        repo_response = repo.get_criminal_records(criminal_records_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3")
        
        assert type(repo_response) == list
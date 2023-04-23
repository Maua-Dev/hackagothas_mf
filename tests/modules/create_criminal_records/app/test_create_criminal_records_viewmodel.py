from src.modules.create_criminal_records.app.create_criminal_records_viewmodel import CreateCriminalRecordsViewModel
from src.shared.infra.repositories.criminal_records_repository_mock import CriminalRecordsRepositoryMock


class Test_CreateCriminalRecordsViewModel:
    def test_create_criminal_records_viewmodel(self):
        repo = CriminalRecordsRepositoryMock()

        criminal_records = repo.criminal_records[0]

        criminal_records_viewmodel = CreateCriminalRecordsViewModel(criminal_records).to_dict()

        assert criminal_records_viewmodel == {erro aqui papai}
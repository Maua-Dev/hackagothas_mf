import pytest
from hackagothas_mf.src.modules.create_criminal_records.app.create_criminal_records_usecase import CreateCriminalRecordsUseCase
from hackagothas_mf.src.shared.domain.entities.criminal import Criminal
from hackagothas_mf.src.shared.domain.entities.criminal_records import CriminalRecords
from hackagothas_mf.src.shared.domain.enums.criminal_type import CRIME_TYPE
from hackagothas_mf.src.shared.domain.repositories.criminal_records_repository_interface import ICriminalRecordsRepository
from hackagothas_mf.src.shared.helpers.errors.usecase_errors import ForbiddenAction
from hackagothas_mf.src.shared.infra.repositories.criminal_records_repository_mock import CriminalRecordsRepositoryMock


class Test_CreateCriminalRecordsUseCase:
    def test_create_criminal_records_usecase(self):
        repository = CriminalRecordsRepositoryMock()
        usecase = CreateCriminalRecordsUseCase(repository)
        
        criminal_record = CriminalRecords(
                criminal_records_id="13c0dc0a-b79f-4658-8848-b21198e0986f",
                arrested=True,
                crime_type=CRIME_TYPE.DRUG_TRAFFICKING,
                criminal=self.criminal[1])
        
        len_bef = len(repository.criminal_records)
        
        criminal_record_response = usecase(criminal_record=criminal_record)

        len_aft = len(repository.criminal_records)

        assert len_aft == len_bef + 1
        assert criminal_record_response == criminal_record
    
    def test_create_criminal_records_usecase_criminal_record_id_already_exists(self):
        repository = CriminalRecordsRepositoryMock()
        usecase = CreateCriminalRecordsUseCase(repository)

        criminal_record = CriminalRecords(
                criminal_records_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3",
                arrested=True,
                crime_type=CRIME_TYPE.DRUG_TRAFFICKING,
                criminal=self.criminal[1])
        with pytest.raises(ForbiddenAction):
            criminal_records_response = usecase(criminal_record=criminal_record)
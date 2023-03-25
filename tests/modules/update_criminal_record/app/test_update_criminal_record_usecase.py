
import pytest
from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUseCase
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_UpdateCriminalRecordUsecase:
    def test_update_criminal_record_usecase(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUseCase(repo)
        update_criminal_record = usecase(
            criminal_record_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3",
            new_arrested=False,
            new_common_attack_region="Sao Paulo",
            new_crime_type=CRIME_TYPE.DRUG_TRAFFICKING,
            new_description="Rodrigo gosta de traficar",
            new_gender=GENDER.OTHER,
            new_name="Rodrigo"
        )
        
        assert type(update_criminal_record) == CriminalRecord
        
        assert repo.criminal_record[0].criminal_record_id == "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
        assert repo.criminal_record[0].arrested == update_criminal_record.arrested
        assert repo.criminal_record[0].crime_type == update_criminal_record.crime_type
        assert repo.criminal_record[0].criminal.common_attack_region == update_criminal_record.criminal.common_attack_region
        assert repo.criminal_record[0].criminal.description == update_criminal_record.criminal.description
        assert repo.criminal_record[0].criminal.gender == update_criminal_record.criminal.gender
        assert repo.criminal_record[0].criminal.name == update_criminal_record.criminal.name
    
    def test_update_criminal_record_usecase_id_not_found(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUseCase(repo)
        
        with pytest.raises(NoItemsFound):
            update_criminal_record = usecase(
                criminal_record_id="mamaco",
                new_name="Rodrigo"
            )
            
    def test_update_criminal_record_usecase_id_not_string(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUseCase(repo)
        
        with pytest.raises(EntityError):
            update_criminal_record = usecase(
                criminal_record_id=123,
                new_name="Rodrigo"
            )
            
    def test_update_criminal_record_usecase_arrested_not_bool(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUseCase(repo)
        
        with pytest.raises(EntityError):
            update_criminal_record = usecase(
                criminal_record_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3",
                new_name="Rodrigo",
                new_arrested=123
            )
    
    def test_update_criminal_record_usecase_crime_invalid_enum(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUseCase(repo)
        
        with pytest.raises(EntityError):
            update_criminal_record = usecase(
                criminal_record_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3",
                new_crime_type="mamaco",
                new_name="Rodrigo"
            )
    
    
            
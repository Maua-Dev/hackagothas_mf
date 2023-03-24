from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class GetCriminalRecordUseCase:
    def __init__(self, crimnal_record_repository: ICriminalRecordRepository):
        self.repository = crimnal_record_repository

    def __call__(self, criminal_record_id) -> CriminalRecord:
        if CriminalRecord.validate_criminal_record_id(criminal_record_id) == False:
            raise EntityError("criminal_record_id")
        
        criminal_record = self.repository.get_criminal_record(criminal_record_id=criminal_record_id)
        if criminal_record == None:
            raise NoItemsFound("criminal_record_id")
        
        return criminal_record
        
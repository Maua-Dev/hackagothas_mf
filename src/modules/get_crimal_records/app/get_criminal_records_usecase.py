from src.shared.domain.entities.criminal_records import CriminalRecords
from src.shared.domain.repositories.criminal_records_repository_interface import ICriminalRecordsRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetCriminalRecordsUseCase:
    def __init__(self, crimnal_records_repository: ICriminalRecordsRepository):
        self.repository = crimnal_records_repository

    def __call__(self, criminal_records_id) -> CriminalRecords:
        if criminal_records_id == None:
            raise EntityError("criminal_records_id")
        if type(criminal_records_id) != str:
            raise EntityError("criminal_records_id")
        if criminal_records_id == "":
            raise EntityError("criminal_records_id")
        
        criminal_record = self.repository.get_criminal_records(criminal_records_id=criminal_records_id)
        if criminal_record == None:
            raise NoItemsFound("criminal_records_id")
        
        return criminal_record
        
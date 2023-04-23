import uuid
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_records import CriminalRecords
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.repositories.criminal_records_repository_interface import ICriminalRecordsRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class CreateCriminalRecordsUseCase:
    def __init__(self, criminal_records_repository: ICriminalRecordsRepository):
     self.repository = criminal_records_repository

    def __call__(self, criminal_record: CriminalRecords):
       if self.repository.get_criminal_records(criminal_record.criminal_records_id) is not None:
          raise ForbiddenAction("criminal_records_id")
       
       return self.repository.create_criminal_records(criminal_record)
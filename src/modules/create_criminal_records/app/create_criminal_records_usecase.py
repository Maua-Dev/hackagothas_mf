import uuid
from hackagothas_mf.src.shared.domain.entities.criminal import Criminal
from hackagothas_mf.src.shared.domain.entities.criminal_records import CriminalRecords
from hackagothas_mf.src.shared.domain.enums.criminal_type import CRIME_TYPE
from hackagothas_mf.src.shared.domain.repositories.criminal_records_repository_interface import ICriminalRecordsRepository


class CreateCriminalRecordsUseCase:
    def __init__(self, crimnal_records_repository: ICriminalRecordsRepository):
     self.repository = crimnal_records_repository

    def __call__(self, criminal: Criminal, crime_type: CRIME_TYPE, arrested: bool) -> CriminalRecords:
       criminal_records_id = str(uuid.uuid4())
       criminal_record = CriminalRecords(criminal_records_id=criminal_records_id, criminal=criminal, crime_type=crime_type, arrested=arrested )
       return self.repository.create_criminal_records(criminal_record)
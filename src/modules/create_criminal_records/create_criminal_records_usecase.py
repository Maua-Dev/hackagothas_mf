from hackagothas_mf.src.shared.domain.entities.criminal_records import CriminalRecords
from hackagothas_mf.src.shared.domain.repositories.criminal_records_repository_interface import ICriminalRecordsRepository


class CreateCriminalRecordsUsecase:
    def __init__(self,repo_criminal_records: ICriminalRecordsRepository):
        self.repo = repo_criminal_records
    
    def __call__(self, criminal_record: CriminalRecords):
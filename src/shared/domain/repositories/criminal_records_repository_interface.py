from abc import ABC, abstractmethod

from src.shared.domain.entities.criminal_records import CriminalRecords

class ICriminalRecordsRepository(ABC):
    
    @abstractmethod
    def get_criminal_records(self, criminal_records_id: str) -> list:
        pass
    
    @abstractmethod
    def create_criminal_records(self, create_records: CriminalRecords) -> CriminalRecords:
        pass
    

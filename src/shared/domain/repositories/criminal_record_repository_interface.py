from abc import ABC, abstractmethod

from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER

class ICriminalRecordRepository(ABC):
    
    @abstractmethod
    def get_criminal_record(self, criminal_record_id: str) -> list:
        pass
    
    @abstractmethod
    def update_criminal_record(self, criminal_record_id: str, new_arrested: bool = None, 
                                new_crime_type: CRIME_TYPE = None, new_name: str = None, 
                                new_common_attack_region: str = None, new_description: str = None, 
                                new_gender: GENDER = None) -> None:
        pass
    
    

import abc
from src.shared.domain.entities.criminal import Criminal

from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.helpers.errors.domain_errors import EntityError

class CriminalRecord(abc.ABC):
    criminal_record_id: str #uuid
    criminal: Criminal
    crime_type: CRIME_TYPE
    arrested: bool
    
    def __init__(self, criminal_record_id: str, criminal: Criminal, crime_type: CRIME_TYPE, arrested: bool):
        if not self.validate_criminal_record_id(criminal_record_id):
            raise EntityError("criminal_record_id")
        self.criminal_record_id = criminal_record_id  
        
        if not self.validate_criminal(criminal):
            raise EntityError("criminal")
        self.criminal = criminal
        
        if not self.validate_crime_type(crime_type):
            raise EntityError("crime_type")
        self.crime_type = crime_type
        
        if not self.validate_arrested(arrested):
            raise EntityError("arrested must be a bool")
        self.arrested = arrested
    
    @staticmethod
    def validate_criminal_record_id(criminal_record_id: str) -> bool:
        if type(criminal_record_id) is not str:
            return False
        if criminal_record_id is None:
            return False
        if len(criminal_record_id) != 36:
            return False
        return True
    
    @staticmethod
    def validate_criminal(criminal: Criminal) -> bool:
        if type(criminal) is not Criminal:
            return False
        if criminal is None:
            return False
        return True

    @staticmethod
    def validate_crime_type(crime_type: CRIME_TYPE) -> bool:
        if type(crime_type) is not CRIME_TYPE:
            return False
        if crime_type is None:
            return False
        return True

    @staticmethod
    def validate_arrested(arrested: bool) -> bool:
        if type(arrested) is not bool:
            return False
        if arrested is None:
            return False
        return True


        
    
    
    
    

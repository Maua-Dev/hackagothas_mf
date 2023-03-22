import abc

from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.criminal_type import CRIMINAL_TYPE
from src.shared.helpers.errors.domain_errors import EntityError

class Crime(abc):
    crime_id: str #uuid
    criminal: Criminal
    crime_type: CRIMINAL_TYPE
    
    def __init__(self, crime_id: str, criminal: Criminal, crime_type: CRIMINAL_TYPE):
        if not self.validate_crime_id(crime_id):
            raise EntityError("crime_id")
        self.crime_id = crime_id
        
        if not self.validate_criminal(criminal):
            raise EntityError("criminal")
        self.criminal = criminal
        
        if not self.validate_crime_types(crime_type):
            raise EntityError("crime_types")
        self.crime_types = crime_type
        
        @staticmethod
        def validate_crime_id(crime_id: str) -> bool:
            if type(crime_id) is not str:
                return False
            if crime_id is None:
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
        def validate_crime_types(crime_types: CRIMINAL_TYPE) -> bool:
            if type(crime_types) is not CRIMINAL_TYPE:
                return False
            if crime_types is None:
                return False
            return True
        
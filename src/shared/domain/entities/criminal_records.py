import abc
from src.shared.domain.entities.criminal import Criminal

from src.shared.domain.enums.criminal_type import CRIMINAL_TYPE

class CriminalRecords(abc):
    criminal_records_id: str #uuid
    criminal: Criminal
    crime_types: CRIMINAL_TYPE
    arrested: bool
    
    
    
    

from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_records import CriminalRecords
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER

class CriminalViewmodel:
    name: str
    description: str
    gender: GENDER
    common_attack_region: str
    
    def __init__(self, criminal: Criminal):
        self.name = criminal.name
        self.description = criminal.description
        self.gender = criminal.gender
        self.common_attack_region = criminal.common_attack_region
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "gender": self.gender.value,
            "common_attack_region": self.common_attack_region,
        }

class CriminalRecordsViewmodel:
    criminal_records_id: str #uuid
    criminal: CriminalViewmodel
    crime_type: CRIME_TYPE
    arrested: bool
    
    def __init__(self, criminal_records: CriminalRecords):
        self.criminal_records_id = criminal_records.criminal_records_id
        self.criminal = CriminalViewmodel(criminal_records.criminal)
        self.crime_type = criminal_records.crime_type
        self.arrested = criminal_records.arrested
    
    def to_dict(self):
        return {
            "criminal_records_id": self.criminal_records_id,
            "criminal": self.criminal.to_dict(),
            "crime_type": self.crime_type.value,
            "arrested": self.arrested,
        }

class GetCriminalRecordsViewmodel:
    criminal_records: CriminalRecordsViewmodel
    
    def __init__(self, criminal_records: CriminalRecords):
        self.criminal_records = CriminalRecordsViewmodel(criminal_records)
    
    def to_dict(self):
        return {
            "criminal_records": self.criminal_records.to_dict(),
            "message": "CriminalRecord was retrieved"
        }
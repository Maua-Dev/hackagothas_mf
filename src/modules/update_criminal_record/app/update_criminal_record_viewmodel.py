from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
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

class CriminalRecordViewmodel:
    criminal_record_id: str #uuid
    criminal: CriminalViewmodel
    crime_type: CRIME_TYPE
    arrested: bool
    
    def __init__(self, criminal_record: CriminalRecord):
        self.criminal_record_id = criminal_record.criminal_record_id
        self.criminal = CriminalViewmodel(criminal_record.criminal)
        self.crime_type = criminal_record.crime_type
        self.arrested = criminal_record.arrested
    
    def to_dict(self):
        return {
            "criminal_record_id": self.criminal_record_id,
            "criminal": self.criminal.to_dict(),
            "crime_type": self.crime_type.value,
            "arrested": self.arrested,
        }


class UpdateCriminalRecordViewModel:
    update_criminal_record: CriminalRecordViewmodel
    
    def __init__(self, update_criminal_record: CriminalRecord):
        self.update_criminal_record_usecase = CriminalRecordViewmodel(update_criminal_record)
    
    def to_dict(self):
        return {
            "criminal_record": self.update_criminal_record_usecase.to_dict(),
            "message": "CriminalRecord was updated"
        }
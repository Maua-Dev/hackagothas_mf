from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_records import CriminalRecords
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER

class CriminalViewModel:
    name: str
    description: str
    gender: GENDER
    common_attack_region: str

    def __init__(self,criminal: Criminal):
        self.name = criminal.name
        self.description = criminal.description
        self.gender = criminal.gender.value
        self.common_attack_region = criminal.common_attack_region
    
    def to_dict(self):
        return{
            "name": self.name,
            "description": self.description,
            "gender": self.gender,
            "common_attack_region": self.common_attack_region
        }

class CriminalRecordViewModel:
    criminal_records_id: str #uuid
    criminal: CriminalViewModel
    crime_type: CRIME_TYPE
    arrested: bool

    def __init__(self,criminal_record: CriminalRecords): 
        self.criminal_records_id = criminal_record.criminal_records_id
        self.criminal = CriminalViewModel(criminal_record.criminal)
        self.crime_type = criminal_record.crime_type
        self.arrested = criminal_record.arrested

    def to_dict(self):
        return{
            "criminal_records_id": self.criminal_records_id,
            "criminal": self.criminal.to_dict(),
            "crime_type": self.crime_type.value,
            "arrested": self.arrested
        }
    
class CreateCriminalRecordsViewModel:
    criminal_record: CriminalRecordViewModel

    def __init__(self, criminal_record: CriminalRecords):
        self.criminal_record = CreateCriminalRecordsViewModel(criminal_record)

    def to_dict(self):
        return{
            "criminal_record": self.criminal_record.to_dict(),
            "message": "the criminal record was created" 
        }
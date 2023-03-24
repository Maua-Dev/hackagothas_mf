from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository


class CriminalRecordRepositoryMock(ICriminalRecordRepository):
    criminal_record: list[CriminalRecord]
    
    criminal: list[Criminal]
    
    def __init__(self):
        self.criminal = [
            Criminal(
                name="Digao",
                common_attack_region="Santo Andre",
                description="Digao gosta de roubar",
                gender=GENDER.MALE
            ),
            Criminal(
                name="Lounis",
                common_attack_region="Suzano",
                description="Lounis gosta de traficar",
                gender=GENDER.MALE
            ),
            Criminal(
                name="Bia",
                common_attack_region="Sao Caetano",
                description="Bia gosta de traficar",
                gender=GENDER.FEMALE
            ),
            Criminal(
                name="Sofia",
                common_attack_region="Sao Bernardo",
                description="Sofia gosta de matar",
                gender=GENDER.FEMALE
            ),
        ]
        
        self.criminal_record = [
            CriminalRecord(
                criminal_record_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3",
                arrested=True,
                crime_type=CRIME_TYPE.ROBBERY,
                criminal=self.criminal[0]
            ),
            CriminalRecord(
                criminal_record_id="13c0dc0a-b79f-4658-8848-b21198e0986f",
                arrested=True,
                crime_type=CRIME_TYPE.DRUG_TRAFFICKING,
                criminal=self.criminal[1]
            ),
            CriminalRecord(
                criminal_record_id="ede0ba42-61e0-434a-9d25-a26d5e31e68d",
                arrested=True,
                crime_type=CRIME_TYPE.DRUG_TRAFFICKING,
                criminal=self.criminal[2]
            ),
            CriminalRecord(
                criminal_record_id="4b276259-43d6-44f6-917b-e3091b880340",
                arrested=True,
                crime_type=CRIME_TYPE.MURDER,
                criminal=self.criminal[3]
            ),
            
            
        ]
    
    def get_criminal_record(self, criminal_record_id: str) -> CriminalRecord:
        for record in self.criminal_record:
            if (record.criminal_record_id == criminal_record_id):
                return record
        return None
    
    def update_criminal_record(self, criminal_record_id: str, new_arrested: bool = None, 
                                new_crime_type: CRIME_TYPE = None, new_name: str = None, 
                                new_common_attack_region: str = None, new_description: str = None, 
                                new_gender: GENDER = None) -> CriminalRecord:
        for record in self.criminal_record:
            if record.criminal_record_id == criminal_record_id:
                if new_crime_type is not None:
                    record.crime_type = new_crime_type
                if new_arrested is not None:
                    record.arrested = new_arrested
                if new_name is not None:
                    record.criminal.name = new_name
                if new_common_attack_region is not None:
                    record.criminal.common_attack_region = new_common_attack_region
                if new_description is not None:
                    record.criminal.description = new_description
                if new_gender is not None:
                    record.criminal.gender = new_gender
                    
                return record
        return None
                
            
        
    
    
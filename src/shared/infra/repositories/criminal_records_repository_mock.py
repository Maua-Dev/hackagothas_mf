from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_records import CriminalRecords
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.domain.repositories.criminal_records_repository_interface import ICriminalRecordsRepository


class CriminalRecordsRepositoryMock(ICriminalRecordsRepository):
    criminal_records: list[CriminalRecords]
    
    criminal: list[Criminal]
    
    def __init__(self):
        self.criminal = [
            Criminal(
                name="Digão",
                common_attack_region="Santo André",
                description="Digão gosta de roubar",
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
                common_attack_region="São Caetano",
                description="Bia gosta de traficar",
                gender=GENDER.FEMALE
            ),
            Criminal(
                name="Sofia",
                common_attack_region="São Bernardo",
                description="Sofia gosta de matar",
                gender=GENDER.FEMALE
            ),
        ]
        
        self.criminal_records = [
            CriminalRecords(
                criminal_records_id="e5a328bb-8522-4530-aa5a-c879a2d87bf3",
                arrested=True,
                crime_type=CRIME_TYPE.ROBBERY,
                criminal=self.criminal[0]
            ),
            CriminalRecords(
                criminal_records_id="13c0dc0a-b79f-4658-8848-b21198e0986f",
                arrested=True,
                crime_type=CRIME_TYPE.DRUG_TRAFFICKING,
                criminal=self.criminal[1]
            ),
            CriminalRecords(
                criminal_records_id="ede0ba42-61e0-434a-9d25-a26d5e31e68d",
                arrested=True,
                crime_type=CRIME_TYPE.DRUG_TRAFFICKING,
                criminal=self.criminal[2]
            ),
            CriminalRecords(
                criminal_records_id="4b276259-43d6-44f6-917b-e3091b880340",
                arrested=True,
                crime_type=CRIME_TYPE.MURDER,
                criminal=self.criminal[3]
            ),
            
            
        ]
    
    def get_criminal_records(self, criminal_records_id: str) -> list[CriminalRecords]:
        return [record for record in self.criminal_records if record.criminal_records_id == criminal_records_id]
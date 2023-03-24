from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UpdateCriminalRecordUseCase:
    def __init__(self, criminal_record_repository: ICriminalRecordRepository):
        self.repository = criminal_record_repository

    def __call__(self, criminal_record_id: str, new_arrested: bool = None, 
                                new_crime_type: CRIME_TYPE = None, new_name: str = None, 
                                new_common_attack_region: str = None, new_description: str = None, 
                                new_gender: GENDER = None) -> CriminalRecord:
        
        if type(criminal_record_id) != str or None:
            raise EntityError("criminal_record_id")
        
        if type(new_arrested) != bool and new_arrested != None:
            raise EntityError("arrested")
        if type(new_crime_type) != CRIME_TYPE and new_crime_type != None:
            raise EntityError("crime_type")
        if type(new_name) != str and new_name != None:
            raise EntityError("name")
        if type(new_common_attack_region) != str and new_common_attack_region != None:
            raise EntityError("common_attack_region")
        if type(new_description) != str and new_description != None:
            raise EntityError("description")
        if type(new_gender) != GENDER and new_gender != None:
            raise EntityError("gender")
        
        criminal_record = self.repository.get_criminal_record(criminal_record_id)
        
        if criminal_record == None:
            raise NoItemsFound("criminal_record_id")
        
        return self.repository.update_criminal_record(
            criminal_record_id=criminal_record_id,
            new_gender=new_gender,
            new_common_attack_region=new_common_attack_region,
            new_name=new_name,
            new_description=new_description,
            new_arrested=new_arrested,
            new_crime_type=new_crime_type,
            
        )
        
        
        
        
        
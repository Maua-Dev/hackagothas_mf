import abc

from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.errors.domain_errors import EntityError

class Criminal(abc):
    name: str
    description: str
    gender: GENDER
    common_attack_region: str
    
    def __init__(self, name: str, description: str, gender: GENDER, common_attack_region: str):
        if not self.validate_name(name):
            raise EntityError("name")
        self.name = name
        
        if not self.validate_description(description):
            raise EntityError("description")
        self.description = description
        
        if not self.validate_gender(gender):
            raise EntityError("gender")
        self.gender = gender
        
        if not self.validate_common_attack_region(common_attack_region):
            raise EntityError("common_attack_region")
        self.common_attack_region = common_attack_region
        
        @staticmethod
        def validate_name(name: str) -> bool:
            if type(name) is not str:
                return False
            if name is None:
                return False
            return True
        
        @staticmethod
        def validate_description(description: str) -> bool:
            if type(description) is not str:
                return False
            if description is None:
                return False
            return True
        
        @staticmethod
        def validate_gender(gender: GENDER) -> bool:
            if type(gender) is not GENDER:
                return False
            if gender is None:
                return False
            return True
        
        @staticmethod
        def validate_common_attack_region(common_attack_region: str) -> bool:
            if type(common_attack_region) is not str:
                return False
            if common_attack_region is None:
                return False
            return True
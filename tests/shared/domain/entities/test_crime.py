import pytest
import uuid

from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.errors.domain_errors import EntityError

class Test_Crime():
    def test_crime(self):
        generate_uuid = uuid.uuid4()
        criminal = Criminal(name="Digao", common_attack_region="Santo andré", description="Gosta de roubar", gender=GENDER.MALE)
        crime = Crime(crime_id=str(generate_uuid), criminal=criminal, crime_type=CRIME_TYPE.ROBBERY)
        
        assert crime.crime_id == str(generate_uuid)
        assert crime.criminal == criminal
        assert crime.crime_type == CRIME_TYPE.ROBBERY
    
    def test_crime_missing_parameters(self):
        with pytest.raises(EntityError):
            crime = Crime(crime_id=None, criminal=None, crime_type=None)
    
    def test_crime_missing_crime_id(self):
        with pytest.raises(EntityError):
            crime = Crime(crime_id=None, criminal=Criminal(name="Digao", common_attack_region="Santo andré", description="Gosta de roubar", gender=GENDER.MALE), crime_type=CRIME_TYPE.ROBBERY)
    
    def test_crime_missing_criminal(self):
        with pytest.raises(EntityError):
            crime = Crime(crime_id=str(uuid.uuid4()), criminal=None, crime_type=CRIME_TYPE.ROBBERY)
    
    def test_crime_missing_crime_type(self):
        with pytest.raises(EntityError):
            crime = Crime(crime_id=str(uuid.uuid4()), criminal=Criminal(name="Digao", common_attack_region="Santo andré", description="Gosta de roubar", gender=GENDER.MALE), crime_type=None)
    
    def test_crime_invalid_parameters(self):
        with pytest.raises(EntityError):
            crime = Crime(crime_id=1, criminal=1, crime_type=1)
    
    def test_crime_invalid_crime_id(self):
        with pytest.raises(EntityError):
            crime = Crime(crime_id=1, criminal=Criminal(name="Digao", common_attack_region="Santo andré", description="Gosta de roubar", gender=GENDER.MALE), crime_type=CRIME_TYPE.ROBBERY)
    
    def test_crime_invalid_criminal(self):
        with pytest.raises(EntityError):
            crime = Crime(crime_id=str(uuid.uuid4()), criminal=1, crime_type=CRIME_TYPE.ROBBERY)
    
    def test_crime_invalid_crime_type(self):
        with pytest.raises(EntityError):
            crime = Crime(crime_id=str(uuid.uuid4()), criminal=Criminal(name="Digao", common_attack_region="Santo andré", description="Gosta de roubar", gender=GENDER.MALE), crime_type=1) 
        
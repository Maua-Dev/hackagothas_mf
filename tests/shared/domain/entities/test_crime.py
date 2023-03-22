import pytest
import uuid

from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER

class Test_Crime():
    def test_crime(self):
        generate_uuid = uuid.uuid4()
        criminal = Criminal(name="Digao", common_attack_region="Santo andré", description="Gosta de roubar", gender=GENDER.MALE)
        crime = Crime(crime_id=str(generate_uuid), criminal=criminal, crime_type=CRIME_TYPE.ROBBERY)
        
        assert crime.crime_id == str(generate_uuid)
        assert crime.criminal.name == "Digao"
        assert crime.criminal.common_attack_region == "Santo andré"
        assert crime.criminal.description == "Gosta de roubar"
        assert crime.criminal.gender == GENDER.MALE
        assert crime.crime_type == CRIME_TYPE.ROBBERY
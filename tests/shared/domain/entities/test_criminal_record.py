import pytest
import uuid
from src.shared.domain.entities.criminal import Criminal

from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.errors.domain_errors import EntityError

class Test_Criminal_Record():
    def test_criminal_record(self):
        generate_uuid = str(uuid.uuid4())
        criminal = Criminal(name="Digao", common_attack_region="Santo André", description="Digao gosta de roubar", gender=GENDER.MALE)
        criminal_record = CriminalRecord(criminal_record_id=generate_uuid, arrested=False, crime_type=CRIME_TYPE.MURDER, criminal=criminal)
        
        assert criminal_record.arrested == False
        assert criminal_record.crime_type == CRIME_TYPE.MURDER
        assert criminal_record.criminal == criminal
        assert criminal_record.criminal_record_id == generate_uuid
        
    def test_criminal_record_missing_parameters(self):
        with pytest.raises(EntityError):
            criminal_record = CriminalRecord(criminal_record_id=None, arrested=None, crime_type=None, criminal=None)
    
    def test_criminal_record_missing_criminal_record_id(self):
        with pytest.raises(EntityError):
            criminal_record = CriminalRecord(criminal_record_id=None, arrested=False, crime_type=CRIME_TYPE.ROBBERY, criminal=Criminal(name="Digao", common_attack_region="Santo André", description="Digao gosta de roubar", gender=GENDER.MALE))
    
    def test_criminal_record_missing_arrested(self):
        with pytest.raises(EntityError):
            criminal_record = CriminalRecord(criminal_record_id=str(uuid.uuid4()), arrested=None, crime_type=CRIME_TYPE.ROBBERY, criminal=Criminal(name="Digao", common_attack_region="Santo André", description="Digao gosta de roubar", gender=GENDER.MALE))
    
    def test_criminal_record_missing_crime_type(self):
        with pytest.raises(EntityError):
            criminal_record = CriminalRecord(criminal_record_id=str(uuid.uuid4()), arrested=False, crime_type=None, criminal=Criminal(name="Digao", common_attack_region="Santo André", description="Digao gosta de roubar", gender=GENDER.MALE))
    
    def test_criminal_record_missing_criminal(self):
        with pytest.raises(EntityError):
            criminal_record = CriminalRecord(criminal_record_id=str(uuid.uuid4()), arrested=False, crime_type=CRIME_TYPE.ROBBERY, criminal=None)
    
    def test_criminal_record_invalid_parameters(self):
        with pytest.raises(EntityError):
            criminal_record = CriminalRecord(criminal_record_id=1, arrested=1, crime_type=1, criminal=1)
    
    def test_criminal_record_invalid_criminal_record_id(self):
        with pytest.raises(EntityError):
            criminal_record = CriminalRecord(criminal_record_id=1, arrested=False, crime_type=CRIME_TYPE.ROBBERY, criminal=Criminal(name="Digao", common_attack_region="Santo André", description="Digao gosta de roubar", gender=GENDER.MALE))
    
    def test_criminal_record_invalid_arrested(self):
        with pytest.raises(EntityError):
            criminal_record = CriminalRecord(criminal_record_id=str(uuid.uuid4()), arrested=1, crime_type=CRIME_TYPE.ROBBERY, criminal=Criminal(name="Digao", common_attack_region="Santo André", description="Digao gosta de roubar", gender=GENDER.MALE))
    
    def test_criminal_record_invalid_crime_type(self):
        with pytest.raises(EntityError):
            criminal_record = CriminalRecord(criminal_record_id=str(uuid.uuid4()), arrested=False, crime_type=None, criminal=Criminal(name="Digao", common_attack_region="Santo André", description="Digao gosta de roubar", gender=GENDER.MALE))
            
    def test_criminal_record_invalid_criminal(self):
        with pytest.raises(EntityError):
            criminal_record = CriminalRecord(criminal_record_id=str(uuid.uuid4()), arrested=False, crime_type=CRIME_TYPE.ROBBERY, criminal=1)
import pytest

from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.gender import GENDER
from src.shared.helpers.errors.domain_errors import EntityError

class Test_Criminal():
    def test_criminal(self):
        criminal = Criminal(name="Digao", common_attack_region="Santo andré", description="Digao gosta de roubar", gender=GENDER.MALE)
        
        assert criminal.name == "Digao"
        assert criminal.common_attack_region == "Santo andré"
        assert criminal.description == "Digao gosta de roubar"
        assert criminal.gender == GENDER.MALE
        
    def test_criminal_missing_parameters(self):
        with pytest.raises(EntityError):
            criminal = Criminal(name=None, common_attack_region=None, description=None, gender=None)
    
    def test_criminal_missing_name(self):
        with pytest.raises(EntityError):
            criminal = Criminal(name=None, common_attack_region="Santo André", description="Digão gosta de roubar", gender=GENDER.MALE)
    
    def test_criminal_missing_common_attack_region(self):
        with pytest.raises(EntityError):
            criminal = Criminal(name="Digão", common_attack_region=None, description="Digão gosta de roubar", gender=GENDER.MALE)
    
    def test_criminal_missing_description(self):
        with pytest.raises(EntityError):
            criminal = Criminal(name="Digão", common_attack_region="Santo André", description=None, gender=GENDER.MALE)
    
    def test_criminal_missing_gender(self):
        with pytest.raises(EntityError):
            criminal = Criminal(name="Digão", common_attack_region="Santo André", description="Digão gosta de roubar", gender=None)
    
    def test_criminal_invalid_parameters(self):
        with pytest.raises(EntityError):
            criminal = Criminal(name=1, common_attack_region=1, description=1, gender=1)
    
    def test_criminal_invalid_name(self):
        with pytest.raises(EntityError):
            criminal = Criminal(name=1, common_attack_region="Santo André", description="Digão gosta de roubar", gender=GENDER.MALE)
    
    def test_criminal_invalid_length_name(self):
        with pytest.raises(EntityError):
            criminal = Criminal(name="e", common_attack_region=None, description=None, gender=None)
            
    def test_criminal_invalid_common_attack_region(self):
        with pytest.raises(EntityError):
            criminal = Criminal(name="Digão", common_attack_region=1, description="Digão gosta de roubar", gender=GENDER.MALE)
    
    def test_criminal_invalid_length_common_attack_region(self):
        with pytest.raises(EntityError):
            criminal = Criminal(name="Digão", common_attack_region="e", description="Digão gosta de roubar", gender=GENDER.MALE)
    
    def test_criminal_invalid_gender(self):
        with pytest.raises(EntityError):
            criminal = Criminal(name="Digão", common_attack_region="Santo André", description="Digão gosta de roubar", gender=1)
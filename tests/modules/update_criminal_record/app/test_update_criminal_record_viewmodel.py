import pytest
from src.modules.update_criminal_record.app.update_criminal_record_viewmodel import UpdateCriminalRecordViewModel
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_UpdateCriminalRecordViewmodel:
    def test_update_criminal_record_viewmodel(self):
        repo = CriminalRecordRepositoryMock()
        
        criminal_record = repo.update_criminal_record(
            criminal_record_id='e5a328bb-8522-4530-aa5a-c879a2d87bf3',
            new_name='Rodrigo',
            new_description='Rodrigo gosta de traficar',
            new_common_attack_region='Sao Paulo',
            new_gender=GENDER.OTHER,
            new_arrested=False,
            new_crime_type=CRIME_TYPE.DRUG_TRAFFICKING
        )
        viewmodel = UpdateCriminalRecordViewModel(criminal_record).to_dict()
        
        
        expected = {
            'criminal_record':{
                'criminal_record_id':'e5a328bb-8522-4530-aa5a-c879a2d87bf3',
                'criminal':{
                    'name':'Rodrigo',
                    'description':'Rodrigo gosta de traficar',
                    'gender':'OTHER',
                    'common_attack_region':'Sao Paulo'
                },
                'crime_type':'DRUG_TRAFFICKING',
                'arrested': False
            },
            'message':'CriminalRecord was updated'
        }
        
        assert viewmodel == expected        
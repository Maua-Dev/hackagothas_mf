from src.modules.get_crimal_record.app.get_criminal_record_viewmodel import GetCriminalRecordViewmodel
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock
import pyperclip

class Test_GetCriminalRecordViewmodel:
    def test_get_criminal_record_viewmodel(self):
        repo = CriminalRecordRepositoryMock()

        criminal_record = repo.criminal_record[0]
        
        criminal_record_viewmodel = GetCriminalRecordViewmodel(criminal_record).to_dict()       

        assert criminal_record_viewmodel == {
            'criminal_record':{
                'criminal_record_id':'e5a328bb-8522-4530-aa5a-c879a2d87bf3',
                'criminal':{
                    'name':'Digao',
                    'description':'Digao gosta de roubar',
                    'gender':'MALE',
                    'common_attack_region':'Santo Andre'
                },
                'crime_type':'ROBBERY',
                'arrested':True
            },
            'message':'CriminalRecord was retrieved'
        }
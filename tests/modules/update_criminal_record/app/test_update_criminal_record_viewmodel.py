from src.modules.update_criminal_record.app.update_criminal_record_viewmodel import UpdateCriminalRecordViewModel
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_UpdateCriminalRecordViewmodel:
    def test_update_criminal_record_viewmodel(self):
        repo = CriminalRecordRepositoryMock()
        
        criminal_record = repo.criminal_record[0]
        viewmodel = UpdateCriminalRecordViewModel(criminal_record).to_dict()
        
        
        expected = {
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
            'message':'CriminalRecord was updated'
        }
        
        assert viewmodel == expected
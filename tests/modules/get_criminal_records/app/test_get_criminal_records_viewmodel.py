from src.modules.get_crimal_records.app.get_criminal_records_viewmodel import GetCriminalRecordsViewmodel
from src.shared.domain.enums.criminal_type import CRIME_TYPE
from src.shared.domain.enums.gender import GENDER
from src.shared.infra.repositories.criminal_records_repository_mock import CriminalRecordsRepositoryMock


class Test_GetCriminalRecordsViewmodel:
    def test_get_criminal_records_viewmodel(self):
        repo = CriminalRecordsRepositoryMock()

        criminal_records = repo.criminal_records[0]
        
        criminal_records_viewmodel = GetCriminalRecordsViewmodel(criminal_records).to_dict()       

        assert criminal_records_viewmodel == {
            'criminal_records':{
                'criminal_records_id':'e5a328bb-8522-4530-aa5a-c879a2d87bf3',
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
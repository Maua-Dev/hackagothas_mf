import json
from src.modules.get_crimal_records.app.get_criminal_records_presenter import get_criminal_records_presenter


class Test_GetCriminalRecordsPresenter:
    def test_get_criminal_records_presenter(self):
        event = {
            "body": {
                "criminal_records_id": "e5a328bb-8522-4530-aa5a-c879a2d87bf3"
            }
        }
        
        response = get_criminal_records_presenter(event, None)
        
        expects = {
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
                
        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expects
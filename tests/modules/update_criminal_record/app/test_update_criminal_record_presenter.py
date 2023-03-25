import json

from src.modules.update_criminal_record.app.update_criminal_record_presenter import update_criminal_record_presenter


class Test_UpdateCriminalRecordPresenter:
    def test_update_criminal_record_presenter(self):
        event = {
            "body": {
                "criminal_record_id": "e5a328bb-8522-4530-aa5a-c879a2d87bf3",
                "new_name": "Rodrigo",
                "new_description": "Rodrigo gosta de traficar",
                "new_gender": "OTHER",
                "new_common_attack_region": "Sao Paulo",
                "new_crime_type": "MURDER",
                "new_arrested": False
            }
        }
        
        response = update_criminal_record_presenter(event, None)
        
        expects = {
            'criminal_record':{
                'criminal_record_id':'e5a328bb-8522-4530-aa5a-c879a2d87bf3',
                'criminal':{
                    'name':'Rodrigo',
                    'description':'Rodrigo gosta de traficar',
                    'gender':'OTHER',
                    'common_attack_region':'Sao Paulo'
                },
                'crime_type':'MURDER',
                'arrested': False
            },
            'message':'CriminalRecord was updated'
        }
                
        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expects
        
    def test_update_criminal_record_presenter_missing_id(self):
        event = {
            "body": {
                "new_name": "Rodrigo",
                "new_description": "Rodrigo gosta de traficar",
                "new_gender": "OTHER",
                "new_common_attack_region": "Sao Paulo",
                "new_crime_type": "MURDER",
                "new_arrested": False
            }
        }
        
        response = update_criminal_record_presenter(event, None)
                
        assert response["status_code"] == 400
    
    def test_update_criminal_record_presenter_no_items_found(self):
        event = {
            "body": {
                "criminal_record_id": "mamaco",
                "new_name": "Rodrigo",
                "new_description": "Rodrigo gosta de traficar",
                "new_gender": "OTHER",
                "new_common_attack_region": "Sao Paulo",
                "new_crime_type": "MURDER",
                "new_arrested": False
            }
        }
        
        response = update_criminal_record_presenter(event, None)
                
        assert response["status_code"] == 404

    

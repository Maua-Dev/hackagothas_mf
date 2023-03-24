from fastapi import FastAPI

from src.modules.get_crimal_record.app.get_criminal_record_presenter import get_criminal_record_presenter

app = FastAPI()

@app.get("/get_criminal_record_by_id")
def get_criminal_record_by_id(criminal_record_id=None):
    event = {
        "body": {},
        "headers": {},
        "query_params": {
            "criminal_record_id": criminal_record_id
        }
    }
    
    response = get_criminal_record_presenter(event, None)
    
    return response
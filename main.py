from fastapi import FastAPI

from src.modules.get_crimal_records.app.get_criminal_records_presenter import get_criminal_records_presenter

app = FastAPI()

@app.get("/get_criminal_records_by_id")
def get_criminal_records_by_id(criminal_records_id=None):
    event = {
        "body": {},
        "headers": {},
        "query_params": {
            "criminal_records_id": criminal_records_id
        }
    }
    
    response = get_criminal_records_presenter(event, None)
    
    return response
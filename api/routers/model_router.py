import os
from fastapi import APIRouter
from ..models import ModelItem
from joblib import load
import pandas as pd

# Find the absolute path of the project root
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the path to the model file
model_path = os.path.join(root_path, 'routers', 'random_forest_model.joblib')
router = APIRouter()

model = load(model_path)
@router.get("/")
async def start_endpoint():
    # Your endpoint logic goes here
    return {"message": "This is an endpoint on diabetes model"}

@router.post("/predict")
async def example_endpoint(item: ModelItem):
    # Load the model
    data = {'discharge_disposition_id': 6,
            'time_in_hospital': 11,
            'num_medications': 18,
            'number_outpatient': 0,
            'number_emergency': 1,
            'number_inpatient': 0,
            'number_diagnoses': 9,
            'change': 0,
            'diabetesMed': 1}
    single_instance = pd.DataFrame([data])
    # Make a prediction
    prediction = model.predict(single_instance)
    result = f'The prediction value is {prediction[0]}'
    # Your endpoint logic goes here
    return {"message": result}
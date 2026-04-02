from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI() # app is object

def get_data():
    with open('patients.json', 'r') as file:
        return json.load(file)

@app.get("/")
def hello():
    return { 'message':'Hello world'}

@app.get("/view")
def view():
    data = get_data()
    return data

@app.get('/view/{patient_id}')
def view_patient(patient_id: str = Path(..., description='The ID of the patient to view')):
    data = get_data()
    for patient in data['records']:
        if patient['patient_id'] == patient_id:
            return patient
        raise HTTPException(status_code=404, detail='Patient not found')

@app.get('/patient')
def sort_patients(sort_by: str = Query(..., description='The field to sort by'), order: str = Query(..., description='The order to sort by')):
    valid_fields = ['height_cm', 'weight_kg', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Invalid sort field')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order')

    data = get_data()
    sort_order = True if order == 'asc' else False
    sorted_data = sorted(data['records'], key=lambda x: x[sort_by], reverse=sort_order)

    return sorted_data

@app.get('/about')
def about():
    return {'message':'Hi there! My name is hasib'}
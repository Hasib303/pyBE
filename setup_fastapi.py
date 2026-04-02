from fastapi import FastAPI, Path
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
    return {'error':'Patient not found'}

@app.get('/about')
def about():
    return {'message':'Hi there! My name is hasib'}
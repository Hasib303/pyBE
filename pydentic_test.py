from pydantic import BaseModel


class patient(BaseModel):
    name: str
    age: int

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)


def update_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)

patient_info = {"name": "John Doe", "age": 25}

patient1 = patient(**patient_info)

# insert_patient(patient1)
update_patient_data(patient1)

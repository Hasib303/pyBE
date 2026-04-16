from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import List, Dict, Optional, Annotated


class patient(BaseModel):
    # name: str = Field(..., min_length=3, max_length=100)
    name: str = Annotated[str, Field(min_length=3, title= "Name of the patient", description= "The name of the patient")]
    age: int = Field(..., ge=0, le=120)
    weight: Annotated[float, Field(gt=0, lt=200)]
    allergies: list[str]
    contact_details: dict[str, str]
    email: EmailStr
    linkedin_url: Optional[HttpUrl] = None

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)


def update_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.email)
    print(patient.linkedin_url)

patient_info = {"name": "John", "age": 120, "weight": 70.5, "allergies": ["penicillin", "shellfish"], "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}, "email": "john.doe@example.com", "linkedin_url": "http://linkedin.com/in/john-doe-1234567890"}

patient1 = patient(**patient_info)

# insert_patient(patient1)
update_patient_data(patient1)

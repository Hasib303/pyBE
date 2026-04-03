from pydantic import BaseModel


class patient(BaseModel):
    name: str
    age: int

def insert_patient(name, age):

    print(name)
    print(age)



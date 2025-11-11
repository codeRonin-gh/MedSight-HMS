from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/emergency",
    tags=["Emergency Department"]
)

class Patient(BaseModel):
    id: int
    name: str
    age: int
    condition: str

# Dummy data
patients: List[Patient] = [
    Patient(id=1, name="John Doe", age=30, condition="Severe injury"),
    Patient(id=2, name="Mary Johnson", age=45, condition="Fracture"),
    Patient(id=3, name="Samuel Kofi", age=60, condition="Heart attack"),
    Patient(id=4, name="Linda Mensah", age=27, condition="Burns"),
    Patient(id=5, name="Kwame Appiah", age=50, condition="Stroke")
]

@router.get("/queue", response_model=List[Patient])
def get_queue():
    return patients

@router.post("/register", response_model=Patient)
def register_patient(patient: Patient):
    for p in patients:
        if p.id == patient.id:
            raise HTTPException(status_code=400, detail="Patient ID already exists")
    patients.append(patient)
    return patient

@router.put("/update/{patient_id}")
def update_patient(patient_id: int, condition: str):
    for p in patients:
        if p.id == patient_id:
            p.condition = condition
            return {"message": "Patient updated", "patient": p}
    raise HTTPException(status_code=404, detail="Patient not found")

@router.delete("/delete/{patient_id}")
def delete_patient(patient_id: int):
    for p in patients:
        if p.id == patient_id:
            patients.remove(p)
            return {"message": "Patient removed"}
    raise HTTPException(status_code=404, detail="Patient not found")

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

router = APIRouter(
    prefix="/wards",
    tags=["Inpatient Wards"]
)

# --- Model ---
class PatientAdmission(BaseModel):
    id: int
    name: str
    age: int
    condition: str
    ward: str
    bed_number: Optional[int] = None
    admission_time: datetime = datetime.now()
    status: str = "Admitted"

# --- In-memory storage with dummy data ---
wards_db: List[PatientAdmission] = [
    PatientAdmission(id=201, name="Kwame Appiah", age=50, condition="Pneumonia", ward="General", bed_number=5),
    PatientAdmission(id=202, name="Akosua Adjei", age=30, condition="ICU Care", ward="ICU", bed_number=1),
    PatientAdmission(id=203, name="Kofi Boateng", age=40, condition="Maternity Check", ward="Maternity", bed_number=2),
    PatientAdmission(id=204, name="Ama Serwaa", age=35, condition="Post Surgery", ward="General", bed_number=6),
    PatientAdmission(id=205, name="John Mensah", age=45, condition="Stroke Recovery", ward="ICU", bed_number=2),
]

# --- Endpoints ---

# Admit a patient
@router.post("/admit")
def admit_patient(patient: PatientAdmission):
    for p in wards_db:
        if p.id == patient.id:
            raise HTTPException(status_code=400, detail="Patient ID already admitted")
    if patient.bed_number is None:
        existing_beds = [p.bed_number for p in wards_db if p.ward.lower() == patient.ward.lower() and p.bed_number]
        patient.bed_number = max(existing_beds, default=0) + 1
    wards_db.append(patient)
    return {"message": f"{patient.name} admitted to {patient.ward}, Bed {patient.bed_number}", "patient": patient}

# Get patients in a specific ward
@router.get("/ward/{ward_name}")
def get_ward_patients(ward_name: str):
    patients = [p for p in wards_db if p.ward.lower() == ward_name.lower()]
    return {"ward": ward_name, "patients": patients}

# Update patient status
@router.put("/update/{patient_id}")
def update_status(patient_id: int, status: str):
    for p in wards_db:
        if p.id == patient_id:
            p.status = status
            return {"message": f"{p.name}'s status updated to {status}", "patient": p}
    raise HTTPException(status_code=404, detail="Patient not found")

# Discharge a patient
@router.put("/discharge/{patient_id}")
def discharge_patient(patient_id: int):
    for p in wards_db:
        if p.id == patient_id:
            p.status = "Discharged"
            return {"message": f"{p.name} discharged from {p.ward}, Bed {p.bed_number}", "patient": p}
    raise HTTPException(status_code=404, detail="Patient not found")

# Delete a patient record
@router.delete("/delete/{patient_id}")
def delete_patient(patient_id: int):
    for p in wards_db:
        if p.id == patient_id:
            wards_db.remove(p)
            return {"message": f"{p.name}'s record deleted"}
    raise HTTPException(status_code=404, detail="Patient not found")

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List

router = APIRouter(
    prefix="/opd",
    tags=["Outpatient Clinics"]
)

# --- Model ---
class Appointment(BaseModel):
    id: int
    patient_name: str
    age: int
    condition: str
    doctor: str
    appointment_time: datetime
    status: str = "Scheduled"

# --- In-memory storage with dummy data ---
appointments_db: List[Appointment] = [
    Appointment(id=101, patient_name="Jane Doe", age=28, condition="Fever", doctor="Dr. Mensah", appointment_time=datetime(2025,11,12,10,0)),
    Appointment(id=102, patient_name="Kojo Antwi", age=35, condition="Headache", doctor="Dr. Amoah", appointment_time=datetime(2025,11,12,11,0)),
    Appointment(id=103, patient_name="Ama Serwaa", age=42, condition="Back pain", doctor="Dr. Mensah", appointment_time=datetime(2025,11,12,12,0)),
    Appointment(id=104, patient_name="Kwame Boateng", age=50, condition="Allergy", doctor="Dr. Mensah", appointment_time=datetime(2025,11,12,13,0)),
    Appointment(id=105, patient_name="Linda Mensah", age=30, condition="Sprain", doctor="Dr. Amoah", appointment_time=datetime(2025,11,12,14,0)),
]

# --- Endpoints ---

# Register a new appointment
@router.post("/register")
def register_appointment(appointment: Appointment):
    for a in appointments_db:
        if a.id == appointment.id:
            raise HTTPException(status_code=400, detail="Appointment ID already exists")
    appointments_db.append(appointment)
    return {"message": f"Appointment for {appointment.patient_name} registered.", "appointment": appointment}

# Get all appointments
@router.get("/appointments")
def get_appointments():
    return {"appointments": appointments_db}

# Update appointment status
@router.put("/update/{appointment_id}")
def update_status(appointment_id: int, status: str):
    for a in appointments_db:
        if a.id == appointment_id:
            a.status = status
            return {"message": f"Appointment {a.id} status updated to {status}", "appointment": a}
    raise HTTPException(status_code=404, detail="Appointment not found")

# Delete an appointment
@router.delete("/delete/{appointment_id}")
def delete_appointment(appointment_id: int):
    for a in appointments_db:
        if a.id == appointment_id:
            appointments_db.remove(a)
            return {"message": f"Appointment {a.id} deleted"}
    raise HTTPException(status_code=404, detail="Appointment not found")

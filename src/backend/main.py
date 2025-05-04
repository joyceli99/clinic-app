from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
import database

app = FastAPI()

@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(database.get_db)):
    """Create a new patient record"""
    return models.create_patient(db=db, patient=patient)

@app.post("/appointments/", response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(database.get_db)):
    """Schedule a new appointment"""
    return models.create_appointment(db=db, appointment=appointment)

@app.get("/appointments/{patient_id}", response_model=List[schemas.Appointment])
def get_patient_appointments(patient_id: int, db: Session = Depends(database.get_db)):
    """Retrieve appointments for a specific patient"""
    return models.get_appointments_by_patient(db=db, patient_id=patient_id)

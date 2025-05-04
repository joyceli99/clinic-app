from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import Optional

class PatientBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    patient_id: int
    appointment_date: datetime
    reason: str

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    status: str = "Scheduled"

    class Config:
        orm_mode = True

    @validator('appointment_date')
    def validate_future_date(cls, v):
        if v <= datetime.now():
            raise ValueError('Appointment must be in the future')
        return v

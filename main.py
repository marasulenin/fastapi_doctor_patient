from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(
    title="Doctor and Patient API",
    description="REST API for managing doctors and patients",
    version="1.0.0"
)


# ==================================================
# DOCTOR MODEL
# ==================================================

class Doctor(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


# ==================================================
# PATIENT MODEL
# ==================================================

class Patient(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    phone: str


# ==================================================
# IN-MEMORY STORAGE
# ==================================================

doctors = []
patients = []

doctor_id_counter = 1
patient_id_counter = 1


# ==================================================
# HOME API
# ==================================================

@app.get("/")
def home():
    return {
        "message": "Doctor and Patient API is working"
    }


# ==================================================
# DOCTOR APIs
# ==================================================

# CREATE DOCTOR
@app.post("/doctors")
def create_doctor(doctor: Doctor):

    global doctor_id_counter

    new_doctor = {
        "id": doctor_id_counter,
        "name": doctor.name,
        "specialization": doctor.specialization,
        "email": str(doctor.email),
        "is_active": doctor.is_active
    }

    doctors.append(new_doctor)

    doctor_id_counter += 1

    return {
        "message": "Doctor created successfully",
        "doctor": new_doctor
    }


# GET ALL DOCTORS
@app.get("/doctors")
def get_doctors():

    return {
        "count": len(doctors),
        "doctors": doctors
    }


# GET DOCTOR BY ID
@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):

    for doctor in doctors:

        if doctor["id"] == doctor_id:
            return {
                "doctor": doctor
            }

    raise HTTPException(
        status_code=404,
        detail="Doctor not found"
    )


# UPDATE DOCTOR
@app.put("/doctors/{doctor_id}")
def update_doctor(doctor_id: int, doctor: Doctor):

    for existing_doctor in doctors:

        if existing_doctor["id"] == doctor_id:

            existing_doctor["name"] = doctor.name
            existing_doctor["specialization"] = doctor.specialization
            existing_doctor["email"] = str(doctor.email)
            existing_doctor["is_active"] = doctor.is_active

            return {
                "message": "Doctor updated successfully",
                "doctor": existing_doctor
            }

    raise HTTPException(
        status_code=404,
        detail="Doctor not found"
    )


# DELETE DOCTOR
@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int):

    for doctor in doctors:

        if doctor["id"] == doctor_id:

            doctors.remove(doctor)

            return {
                "message": "Doctor deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Doctor not found"
    )


# ==================================================
# PATIENT APIs
# ==================================================

# CREATE PATIENT
@app.post("/patients")
def create_patient(patient: Patient):

    global patient_id_counter

    new_patient = {
        "id": patient_id_counter,
        "name": patient.name,
        "age": patient.age,
        "phone": patient.phone
    }

    patients.append(new_patient)

    patient_id_counter += 1

    return {
        "message": "Patient created successfully",
        "patient": new_patient
    }


# GET ALL PATIENTS
@app.get("/patients")
def get_patients():

    return {
        "count": len(patients),
        "patients": patients
    }


# GET PATIENT BY ID
@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):

    for patient in patients:

        if patient["id"] == patient_id:

            return {
                "patient": patient
            }

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


# UPDATE PATIENT
@app.put("/patients/{patient_id}")
def update_patient(patient_id: int, patient: Patient):

    for existing_patient in patients:

        if existing_patient["id"] == patient_id:

            existing_patient["name"] = patient.name
            existing_patient["age"] = patient.age
            existing_patient["phone"] = patient.phone

            return {
                "message": "Patient updated successfully",
                "patient": existing_patient
            }

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


# DELETE PATIENT
@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):

    for patient in patients:

        if patient["id"] == patient_id:

            patients.remove(patient)

            return {
                "message": "Patient deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )
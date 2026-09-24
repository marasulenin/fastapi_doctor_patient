# FastAPI Doctor and Patient API

A simple REST API built using **FastAPI** and **Pydantic** to manage doctors and patients.

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* REST API
* In-memory storage

## Features

### Doctor APIs

| Method | Endpoint               | Description      |
| ------ | ---------------------- | ---------------- |
| POST   | `/doctors`             | Create a doctor  |
| GET    | `/doctors`             | Get all doctors  |
| GET    | `/doctors/{doctor_id}` | Get doctor by ID |
| PUT    | `/doctors/{doctor_id}` | Update doctor    |
| DELETE | `/doctors/{doctor_id}` | Delete doctor    |

### Patient APIs

| Method | Endpoint                 | Description       |
| ------ | ------------------------ | ----------------- |
| POST   | `/patients`              | Create a patient  |
| GET    | `/patients`              | Get all patients  |
| GET    | `/patients/{patient_id}` | Get patient by ID |
| PUT    | `/patients/{patient_id}` | Update patient    |
| DELETE | `/patients/{patient_id}` | Delete patient    |

## Validation

The API uses Pydantic for request validation.

### Doctor

* Name is required
* Specialization is required
* Email must be a valid email address
* `is_active` defaults to `true`

### Patient

* Name is required
* Age must be greater than 0
* Phone number is required

## Error Handling

The API returns HTTP `404 Not Found` when a requested doctor or patient does not exist.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/marasulenin/fastapi_doctor_patient.git
```

### 2. Open the project

```bash
cd fastapi_doctor_patient
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\activate
```

Git Bash:

```bash
source venv/Scripts/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the server

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically provides interactive Swagger API documentation.

## Storage

This project currently uses **in-memory lists** for storing doctors and patients.

Therefore, data is reset whenever the FastAPI application is restarted.

## Project Structure

```text
fastapi_doctor_patient/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## GitHub Repository

https://github.com/marasulenin/fastapi_doctor_patient

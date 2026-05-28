# CareConnect API Documentation

## Base URL
http://127.0.0.1:8000/patient/api/ (development)
https://careconnect.onrender.com/patient/api/ (production)

## Authentication
Some endpoints require authentication.
Include token in header: Authorization: Token <472da821ae787d2fd512fdb6529987d89fc4b370>

---

## Endpoints

### 1. GET /patient/api/doctors/
Returns list of all verified doctors.
- Auth required: No
- Method: GET
- Response: Array of doctor objects

Example response:
```json
[
  {
    "id": 1,
    "username": "lola",
    "email": "lola@gmail.com",
    "speciality": "dermatology",
    "bio": "Experienced general practitioner",
    "experience": 5,
    "rating": "3.7",
    "is_verified": true
  }
]
```

---

### 2. GET /patient/api/doctors/:id/
Returns details of a single doctor.
- Auth required: No
- Method: GET
- Response: Single doctor object

---

### 3. GET /patient/api/appointments/
Returns all appointments for logged in patient.
- Auth required: Yes
- Method: GET
- Response: Array of appointment objects

### POST /patient/api/appointments/
Create a new appointment.
- Auth required: Yes
- Method: POST
- Body: { doctor, appointment_date, start_time, end_time, notes }

---

### 4. GET /patient/api/appointments/:id/
Returns details of a single appointment.
- Auth required: Yes
- Method: GET

### PUT /patient/api/appointments/:id/
Cancel an appointment.
- Auth required: Yes
- Method: PUT

### DELETE /patient/api/appointments/:id/
Delete an appointment.
- Auth required: Yes
- Method: DELETE

---

### 5. GET /patient/api/notifications/
Returns unread notifications for logged in user.
- Auth required: Yes
- Method: GET
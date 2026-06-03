# CareConnect — Clinic & Appointment Booking System

🌐 **Live Demo:** [https://careconnect-x4wt.onrender.com](https://careconnect-x4wt.onrender.com)

A full-stack clinic and appointment booking web application built with Django and Django REST Framework. Patients can register, browse doctors, and book appointments. Doctors can manage their schedules and patients. Admins have full oversight with reports and user management.

---

## Features

- Role-based authentication — Patient, Doctor, and Admin roles
- Full appointment booking flow with confirmation, editing, and cancellation
- Full CRUD on appointments — create, view, edit, and delete
- Doctor availability management
- Patient prescriptions and profile settings
- Admin dashboard with clinic stats and daily reports
- REST API with token authentication (8 endpoints)
- Flash messages on all key actions
- Deployed on Render with Supabase PostgreSQL

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.14, Django 6.0 |
| Database | Supabase PostgreSQL (production & local) |
| API | Django REST Framework |
| Authentication | Django Auth + DRF Token Authentication |
| Frontend | HTML, CSS (custom design system, no Bootstrap) |
| Fonts & Icons | Poppins (Google Fonts), Font Awesome 6.5 |
| Deployment | Render, Whitenoise, Gunicorn |

---

## Local Setup

**Requirements:** Python 3.14, pip

```bash
# 1. Clone the repo
git clone https://github.com/iyiade08/dune-cohort-final-project.git
cd dune-cohort-final-project/careconnect

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Fill in your values in .env

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Collect static files
python manage.py collectstatic --noinput

# 8. Start the development server
python manage.py runserver
```

Visit http://127.0.0.1:8000

---

## Environment Variables

Create a `.env` file in the project root. See `.env.example` for required variable names:

```
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
DATABASE_URL=
```

---

## Project Structure

```
careconnect/
├── careconnect_config/    # Django settings and URLs
├── core/                  # Marketing pages (home, about, contact)
├── accounts/              # Authentication, user profiles
├── doctors/               # Doctor profiles and availability
├── appointments/          # Booking system and REST API
├── reports/               # Admin dashboard and reports
├── templates/             # All HTML templates
├── static/css/main.css    # Custom CSS design system
├── postman_collection.json
├── requirements.txt
└── manage.py
```

---

## User Roles

**Patient** — Register, browse doctors, book, edit, and delete appointments, view prescriptions

**Doctor** — Manage schedule, set availability, view patient list, mark appointments complete

**Admin** — Full oversight, user management, daily reports, all appointments view. Created via Django admin or shell only.

---

## REST API

Base URL: `https://careconnect-x4wt.onrender.com`

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| GET | `/patient/api/doctors/` | No | List all verified doctors |
| GET | `/patient/api/doctors/<id>/` | No | Get doctor details |
| GET | `/patient/api/appointments/` | Yes | List patient appointments |
| POST | `/patient/api/appointments/` | Yes | Create new appointment |
| GET | `/patient/api/appointments/<id>/` | Yes | Get appointment detail |
| PUT | `/patient/api/appointments/<id>/` | Yes | Cancel appointment |
| DELETE | `/patient/api/appointments/<id>/` | Yes | Delete appointment |
| GET | `/patient/api/notifications/` | Yes | List unread notifications |

**Authentication:** Include this header in protected requests:
```
Authorization: Token your_token_here
```

**Example POST body for creating an appointment:**
```json
{
  "doctor": 1,
  "appointment_date": "2026-07-01",
  "start_time": "10:00:00",
  "end_time": "10:30:00",
  "notes": "Routine checkup"
}
```

See `postman_collection.json` for ready-to-use requests.

---

## Screenshots

![Home Page](screenshots/home.png)
![Patient Dashboard](screenshots/patient_dashboard.png)
![Book Appointment](screenshots/book_appointment.png)
![My Appointments](screenshots/my_appointments.png)
![Admin Dashboard](screenshots/admin_dashboard.png)

---

## Deployment

Deployed on **Render** (free tier) with **Supabase PostgreSQL**.

**Build command:**
```
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

**Start command:**
```
gunicorn careconnect_config.wsgi:application
```

**Required environment variables on Render:**
- `SECRET_KEY`
- `DEBUG` = False
- `ALLOWED_HOSTS` = careconnect-x4wt.onrender.com
- `DATABASE_URL` = your Supabase connection string

---

## Future Improvements

- Email notifications for appointment confirmations and reminders
- Doctor photo upload via profile settings
- Video consultation integration
- Prescription management with PDF export
- Patient medical history tracking
- Mobile app using the existing REST API

---

## Course Info

**Course:** Dune Cohort — Backend Development with Python & Django

**Instructor:** Mr. Ayo Oyewo
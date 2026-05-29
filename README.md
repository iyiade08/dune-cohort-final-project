# CareConnect — Clinic & Appointment Booking System

🌐 **Live Site:** https://careconnect-x4wt.onrender.com

A full-stack clinic and appointment booking web application built with Django and Django REST Framework. Patients can register, browse doctors, and book appointments. Doctors can manage their schedules and patients. Admins have full oversight with reports and user management.

---

## Features

- Role-based authentication — Patient, Doctor, and Admin roles
- Full appointment booking flow with confirmation and cancellation
- Doctor availability management
- Patient prescriptions and profile settings
- Admin dashboard with clinic stats and daily reports
- REST API with token authentication
- Deployed on Render with Supabase PostgreSQL

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.14, Django 6.0 |
| Database | SQLite (dev), Supabase PostgreSQL (production) |
| API | Django REST Framework |
| Frontend | HTML, CSS (custom design system) |
| Fonts & Icons | Poppins, Font Awesome 6.5 |
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

# 7. Start the development server
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

**Patient** — Register, browse doctors, book and cancel appointments, view prescriptions

**Doctor** — Manage schedule, set availability, view patient list, mark appointments complete

**Admin** — Full oversight, user management, daily reports, all appointments view. Created via Django admin or shell only.

---

## REST API

Base URL: `https://careconnect-x4wt.onrender.com`

All endpoints require token authentication. Include this header in every request:
```
Authorization: Token <your_token>
```

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/patient/api/doctors/` | List all doctors |
| GET | `/patient/api/doctors/<id>/` | Doctor detail |
| GET/POST | `/patient/api/appointments/` | List or create appointments |
| GET/DELETE | `/patient/api/appointments/<id>/` | Appointment detail or cancel |
| GET | `/patient/api/notifications/` | User notifications |

See `postman_collection.json` for ready-to-use requests.

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

## Course Info

**Course:** Dune Cohort — Backend Development with Python & Django

**Instructor:** Mr. Ayo Oyewo
# CareConnect 🏥
A modern clinic and appointment booking system built with Django.

## Live URL
Coming soon — will be deployed on Render

## About
CareConnect is a web-based healthcare platform that allows:
- Patients to register and book appointments with doctors
- Doctors to manage their schedules and availability
- Admins to oversee clinic operations and generate reports

## Push Log

### Push 2 - User Model & Settings
- Configured settings.py with installed apps
- Installed Django REST Framework
- Created custom User model with role field
- Registered User model in admin
- Ran migrations
- Created superuser

## Tech Stack
- Python / Django
- Django REST Framework
- HTML, CSS, JavaScript
- SQLite (development) / PostgreSQL (production)

## Setup Instructions
1. Clone the repo
2. cd into careconnect
3. Create virtual environment: `python -m venv venv`
4. Activate: `venv\Scripts\activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run migrations: `python manage.py migrate`
7. Start server: `python manage.py runserver`

## Developer
Built as a final project - Dune Cohort
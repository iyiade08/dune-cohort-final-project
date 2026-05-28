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

### Push 3 - Marketing Home Page

- Built base.html shared layout
- Built full home page with all sections
- Hero, About, Features, Pricing, CTA, Footer
- Configured static files and core URLs
- Applied custom CSS design system

### Push 4 - Authentication Flow

- Built register, login, forgot password pages
- Custom auth forms with role selection
- Users saving correctly to database
- Role-based redirect after login
- Auth CSS styling added to main.css

### Push 5 - Patient & Doctor Dashboards

- Built patient dashboard with stat cards
- Built doctor dashboard with stat cards
- Sidebar navigation for both dashboards
- Quick actions and notifications sections
- Role-based redirects working

### Push 6 - Appointment Booking System
- Built Doctor and Appointment models
- Built booking flow - browse doctors, book, confirm
- My appointments page with upcoming and past
- Cancel appointment functionality
- Notifications on booking


### Push 7 - Admin Dashboard & Reports
- Built admin dashboard with clinic stats
- Built all appointments view with filter
- Built user management page
- Built daily report with date filter
- Role-based access control for admin


### Push 8 - REST API, About, Contact & Final Polish
- Built REST API with 5 endpoints
- Added token authentication
- Built About and Contact pages
- Filled api_docs.md
- Project complete

### Push 9 - Production settings and deployment prep
- Cleaned up settings.py
- Added Whitenoise for static files
- Added Gunicorn for production server
- Ready for Render deployment


### Push 10 - Doctor views and templates complete
- Built doctor appointments page
- Built doctor availability management
- Built doctor patients page
- Complete appointment mark as done feature


## Live URL
Coming soon — deploying to Render

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

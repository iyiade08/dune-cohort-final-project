from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('appointments/', views.doctor_appointments, name='doctor_appointments'),
    path('appointments/<int:apt_id>/complete/', views.complete_appointment, name='complete_appointment'),
    path('availability/', views.doctor_availability, name='doctor_availability'),
    path('patients/', views.doctor_patients, name='doctor_patients'),
]
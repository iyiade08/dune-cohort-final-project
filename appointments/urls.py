from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    # Frontend views
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('book/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('book/<int:doctor_id>/confirm/', views.confirm_booking, name='confirm_booking'),
    path('appointments/', views.my_appointments, name='my_appointments'),
    path('appointments/<int:appointment_id>/cancel/', views.cancel_appointment, name='cancel_appointment'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    path('profile/', views.patient_profile, name='patient_profile'),
    path('appointments/<int:appointment_id>/edit/',   views.edit_appointment,   name='edit_appointment'),
path('appointments/<int:appointment_id>/delete/', views.delete_appointment, name='delete_appointment'),

    # REST API endpoints
    path('api/doctors/', api_views.doctor_list_api, name='api_doctor_list'),
    path('api/doctors/<int:doctor_id>/', api_views.doctor_detail_api, name='api_doctor_detail'),
    path('api/appointments/', api_views.appointment_list_api, name='api_appointment_list'),
    path('api/appointments/<int:appointment_id>/', api_views.appointment_detail_api, name='api_appointment_detail'),
    path('api/notifications/', api_views.notification_list_api, name='api_notification_list'),
]
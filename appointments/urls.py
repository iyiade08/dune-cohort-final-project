from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('book/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('book/<int:doctor_id>/confirm/', views.confirm_booking, name='confirm_booking'),
    path('appointments/', views.my_appointments, name='my_appointments'),
    path('appointments/<int:appointment_id>/cancel/', views.cancel_appointment, name='cancel_appointment'),
]
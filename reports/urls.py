from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('/admin-panel/dashboard/'), name='admin_home'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('appointments/', views.all_appointments, name='all_appointments'),
    path('users/', views.user_management, name='user_management'),
    path('reports/', views.daily_report, name='daily_report'),
]
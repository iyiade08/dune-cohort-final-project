from django.contrib import admin
from .models import Appointment, Notification


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display  = ['patient', 'doctor', 'appointment_date', 'start_time', 'status']
    list_filter   = ['status', 'appointment_date']
    search_fields = ['patient__username', 'doctor__user__username']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'is_read', 'created_at']
    list_filter  = ['is_read']
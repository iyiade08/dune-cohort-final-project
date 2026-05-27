from django.contrib import admin
from .models import DoctorProfile, Schedule


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'speciality', 'experience', 'rating', 'is_verified']
    list_filter  = ['speciality', 'is_verified']
    search_fields = ['user__username', 'user__email']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'day_of_week', 'start_time', 'end_time', 'is_available']
    list_filter  = ['day_of_week', 'is_available']
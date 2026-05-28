from rest_framework import serializers
from .models import DoctorProfile, Schedule


class DoctorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email    = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model  = DoctorProfile
        fields = ['id', 'username', 'email', 'speciality', 'bio', 'experience', 'rating', 'is_verified']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Schedule
        fields = ['id', 'doctor', 'day_of_week', 'start_time', 'end_time', 'slot_duration', 'is_available']
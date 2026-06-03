from rest_framework import serializers
from .models import Appointment, Notification


class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.username', read_only=True)
    doctor_name  = serializers.CharField(source='doctor.user.username', read_only=True)
    speciality   = serializers.CharField(source='doctor.get_speciality_display', read_only=True)

    class Meta:
        model  = Appointment
        fields = [
            'id', 'doctor', 'patient_name', 'doctor_name', 'speciality',
            'appointment_date', 'start_time', 'end_time',
            'status', 'notes', 'created_at'
        ]
        extra_kwargs = {
            'doctor': {'write_only': True},
        }


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Notification
        fields = ['id', 'message', 'is_read', 'created_at']
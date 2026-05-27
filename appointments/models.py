from django.db import models
from accounts.models import User
from doctors.models import DoctorProfile


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor           = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    start_time       = models.TimeField()
    end_time         = models.TimeField()
    status           = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes            = models.TextField(blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['doctor', 'appointment_date', 'start_time']

    def __str__(self):
        return f"{self.patient.username} → Dr. {self.doctor.user.username} on {self.appointment_date}"


class Notification(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message    = models.TextField()
    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.message[:40]}"
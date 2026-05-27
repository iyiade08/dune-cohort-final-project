from django.db import models
from accounts.models import User


class DoctorProfile(models.Model):
    SPECIALITIES = [
        ('general', 'General Practice'),
        ('cardiology', 'Cardiology'),
        ('dermatology', 'Dermatology'),
        ('pediatrics', 'Pediatrics'),
        ('gynecology', 'Gynecology'),
        ('neurology', 'Neurology'),
        ('orthopedics', 'Orthopedics'),
        ('psychiatry', 'Psychiatry'),
    ]

    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    speciality  = models.CharField(max_length=50, choices=SPECIALITIES, default='general')
    bio         = models.TextField(blank=True)
    experience  = models.IntegerField(default=0)
    rating      = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    is_verified = models.BooleanField(default=False)
    photo       = models.ImageField(upload_to='doctors/', blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username} — {self.speciality}"


class Schedule(models.Model):
    DAYS = [
        (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'),
        (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday'),
    ]

    doctor          = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='schedules')
    day_of_week     = models.IntegerField(choices=DAYS)
    start_time      = models.TimeField()
    end_time        = models.TimeField()
    slot_duration   = models.IntegerField(default=30)
    is_available    = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor} — {self.get_day_of_week_display()}"
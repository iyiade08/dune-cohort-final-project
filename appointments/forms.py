from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'start_time', 'end_time', 'notes']
        widgets = {
            'appointment_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'start_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'end_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'notes': forms.Textarea(
                attrs={'rows': 4, 'class': 'form-control',
                       'placeholder': 'Any notes for the doctor...'}
            ),
        }
        labels = {
            'appointment_date': 'Appointment Date',
            'start_time':       'Start Time',
            'end_time':         'End Time',
            'notes':            'Notes (optional)',
        }

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_time')
        end   = cleaned_data.get('end_time')
        if start and end and end <= start:
            raise forms.ValidationError('End time must be after start time.')
        return cleaned_data
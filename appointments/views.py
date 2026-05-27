from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def patient_dashboard(request):
    return render(request, 'appointments/patient_dashboard.html')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment


@login_required
def doctor_dashboard(request):
    return render(request, 'doctors/doctor_dashboard.html')


@login_required
def doctor_appointments(request):
    appointments = Appointment.objects.filter(
        doctor__user=request.user
    ).order_by('appointment_date')
    return render(request, 'doctors/doctor_appointments.html', {
        'appointments': appointments
    })


@login_required
def doctor_availability(request):
    from .models import Schedule
    schedules = Schedule.objects.filter(doctor__user=request.user)
    if request.method == 'POST':
        from .models import DoctorProfile
        doctor = DoctorProfile.objects.get(user=request.user)
        day        = request.POST.get('day_of_week')
        start_time = request.POST.get('start_time')
        end_time   = request.POST.get('end_time')
        Schedule.objects.create(
            doctor=doctor,
            day_of_week=day,
            start_time=start_time,
            end_time=end_time,
        )
        from django.contrib import messages
        messages.success(request, 'Availability updated!')
        return redirect('/doctor/availability/')
    return render(request, 'doctors/doctor_availability.html', {
        'schedules': schedules
    })


@login_required
def doctor_patients(request):
    appointments = Appointment.objects.filter(
        doctor__user=request.user,
        status='completed'
    ).values('patient__username', 'patient__email', 'patient__phone').distinct()
    return render(request, 'doctors/doctor_patients.html', {
        'patients': appointments
    })


@login_required
def complete_appointment(request, apt_id):
    from appointments.models import Appointment
    from django.shortcuts import get_object_or_404
    apt = get_object_or_404(Appointment, id=apt_id, doctor__user=request.user)
    apt.status = 'completed'
    apt.save()
    from django.contrib import messages
    messages.success(request, 'Appointment marked as completed!')
    return redirect('/doctor/appointments/')
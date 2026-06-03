from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
        messages.success(request, 'Availability added!')
        return redirect('/doctor/availability/')
    return render(request, 'doctors/doctor_availability.html', {
        'schedules': schedules
    })


@login_required
def edit_schedule(request, schedule_id):
    from .models import Schedule
    schedule = get_object_or_404(Schedule, id=schedule_id, doctor__user=request.user)
    if request.method == 'POST':
        schedule.day_of_week = request.POST.get('day_of_week')
        schedule.start_time  = request.POST.get('start_time')
        schedule.end_time    = request.POST.get('end_time')
        schedule.save()
        messages.success(request, 'Availability updated!')
        return redirect('/doctor/availability/')
    return render(request, 'doctors/edit_schedule.html', {'schedule': schedule})


@login_required
def delete_schedule(request, schedule_id):
    from .models import Schedule
    schedule = get_object_or_404(Schedule, id=schedule_id, doctor__user=request.user)
    if request.method == 'POST':
        schedule.delete()
        messages.success(request, 'Availability deleted!')
    return redirect('/doctor/availability/')


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
    apt = get_object_or_404(Appointment, id=apt_id, doctor__user=request.user)
    apt.status = 'completed'
    apt.save()
    messages.success(request, 'Appointment marked as completed!')
    return redirect('/doctor/appointments/')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment, Notification
from doctors.models import DoctorProfile
from .forms import AppointmentForm


@login_required
def patient_dashboard(request):
    appointments = Appointment.objects.filter(
        patient=request.user,
        status__in=['pending', 'confirmed']
    ).order_by('appointment_date')[:5]
    notifications = Notification.objects.filter(
        user=request.user,
        is_read=False
    )[:5]
    context = {
        'appointments': appointments,
        'notifications': notifications,
        'upcoming_count': Appointment.objects.filter(patient=request.user, status__in=['pending','confirmed']).count(),
        'completed_count': Appointment.objects.filter(patient=request.user, status='completed').count(),
    }
    return render(request, 'appointments/patient_dashboard.html', context)


@login_required
def book_appointment(request):
    doctors = DoctorProfile.objects.filter(is_verified=True)
    speciality = request.GET.get('speciality', '')
    if speciality:
        doctors = doctors.filter(speciality=speciality)
    context = {
        'doctors': doctors,
        'speciality': speciality,
        'specialities': DoctorProfile.SPECIALITIES,
    }
    return render(request, 'appointments/book_appointment.html', context)


@login_required
def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(DoctorProfile, id=doctor_id)
    return render(request, 'appointments/doctor_detail.html', {'doctor': doctor})


@login_required
def confirm_booking(request, doctor_id):
    doctor = get_object_or_404(DoctorProfile, id=doctor_id)
    if request.method == 'POST':
        date       = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time   = request.POST.get('end_time')
        notes      = request.POST.get('notes', '')
        existing = Appointment.objects.filter(
            doctor=doctor,
            appointment_date=date,
            start_time=start_time
        ).exists()
        if existing:
            messages.error(request, 'That slot is already booked. Please choose another time.')
            return redirect('doctor_detail', doctor_id=doctor_id)
        appointment = Appointment.objects.create(
            patient=request.user,
            doctor=doctor,
            appointment_date=date,
            start_time=start_time,
            end_time=end_time,
            notes=notes,
            status='pending'
        )
        Notification.objects.create(
            user=request.user,
            message=f'Your appointment with Dr. {doctor.user.get_full_name() or doctor.user.username} on {date} at {start_time} has been booked!'
        )
        messages.success(request, 'Appointment booked successfully!')
        return redirect('my_appointments')
    return redirect('book_appointment')


@login_required
def my_appointments(request):
    upcoming = Appointment.objects.filter(
        patient=request.user,
        status__in=['pending', 'confirmed']
    ).order_by('appointment_date')
    past = Appointment.objects.filter(
        patient=request.user,
        status__in=['completed', 'cancelled']
    ).order_by('-appointment_date')
    return render(request, 'appointments/my_appointments.html', {
        'upcoming': upcoming,
        'past': past
    })


@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)
    appointment.status = 'cancelled'
    appointment.save()
    messages.success(request, 'Appointment cancelled successfully.')
    return redirect('my_appointments')



@login_required
def prescriptions(request):
    return render(request, 'appointments/prescriptions.html')


@login_required
def patient_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name  = request.POST.get('last_name', '')
        user.email      = request.POST.get('email', '')
        user.phone      = request.POST.get('phone', '')
        user.save()
        from django.contrib import messages
        messages.success(request, 'Profile updated successfully!')
        return redirect('/patient/profile/')
    return render(request, 'appointments/patient_profile.html')


@login_required
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)

    # Only allow editing pending appointments
    if appointment.status != 'pending':
        messages.error(request, 'Only pending appointments can be edited.')
        return redirect('my_appointments')

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            # Check the new slot isn't already taken by another appointment
            data = form.cleaned_data
            conflict = Appointment.objects.filter(
                doctor=appointment.doctor,
                appointment_date=data['appointment_date'],
                start_time=data['start_time']
            ).exclude(id=appointment.id).exists()

            if conflict:
                messages.error(request, 'That slot is already booked. Please choose another time.')
            else:
                form.save()
                messages.success(request, 'Appointment updated successfully!')
                return redirect('my_appointments')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'appointments/edit_appointment.html', {
        'form': form,
        'appointment': appointment,
    })


@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)

    if request.method == 'POST':
        doctor_name = appointment.doctor.user.get_full_name() or appointment.doctor.user.username
        appointment.delete()
        messages.success(request, f'Appointment with Dr. {doctor_name} has been deleted.')
        return redirect('my_appointments')

    # GET request — show confirmation page
    return render(request, 'appointments/delete_appointment.html', {
        'appointment': appointment,
    })
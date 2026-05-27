from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from accounts.models import User
from appointments.models import Appointment
from doctors.models import DoctorProfile


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'admin':
            from django.shortcuts import redirect
            return redirect('/accounts/login/')
        return view_func(request, *args, **kwargs)
    return wrapper


@admin_required
def admin_dashboard(request):
    today = timezone.now().date()
    context = {
        'total_patients':     User.objects.filter(role='patient').count(),
        'total_doctors':      User.objects.filter(role='doctor').count(),
        'total_appointments': Appointment.objects.count(),
        'today_appointments': Appointment.objects.filter(appointment_date=today).count(),
        'pending':            Appointment.objects.filter(status='pending').count(),
        'completed':          Appointment.objects.filter(status='completed').count(),
        'recent_appointments': Appointment.objects.order_by('-created_at')[:10],
    }
    return render(request, 'reports/admin_dashboard.html', context)


@admin_required
def all_appointments(request):
    appointments = Appointment.objects.all().order_by('-created_at')
    status_filter = request.GET.get('status', '')
    if status_filter:
        appointments = appointments.filter(status=status_filter)
    return render(request, 'reports/all_appointments.html', {
        'appointments': appointments,
        'status_filter': status_filter,
    })


@admin_required
def user_management(request):
    patients = User.objects.filter(role='patient')
    doctors  = User.objects.filter(role='doctor')
    return render(request, 'reports/user_management.html', {
        'patients': patients,
        'doctors':  doctors,
    })


@admin_required
def daily_report(request):
    today = timezone.now().date()
    date_str = request.GET.get('date', str(today))
    appointments = Appointment.objects.filter(
        appointment_date=date_str
    ).order_by('start_time')
    context = {
        'appointments': appointments,
        'date': date_str,
        'total':     appointments.count(),
        'pending':   appointments.filter(status='pending').count(),
        'confirmed': appointments.filter(status='confirmed').count(),
        'completed': appointments.filter(status='completed').count(),
        'cancelled': appointments.filter(status='cancelled').count(),
    }
    return render(request, 'reports/daily_report.html', context)
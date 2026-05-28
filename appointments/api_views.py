from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Appointment, Notification
from .serializers import AppointmentSerializer, NotificationSerializer
from doctors.models import DoctorProfile
from doctors.serializers import DoctorSerializer


@api_view(['GET'])
def doctor_list_api(request):
    doctors = DoctorProfile.objects.filter(is_verified=True)
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def doctor_detail_api(request, doctor_id):
    try:
        doctor = DoctorProfile.objects.get(id=doctor_id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    except DoctorProfile.DoesNotExist:
        return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def appointment_list_api(request):
    if request.method == 'GET':
        appointments = Appointment.objects.filter(patient=request.user)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def appointment_detail_api(request, appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id, patient=request.user)
    except Appointment.DoesNotExist:
        return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        appointment.status = 'cancelled'
        appointment.save()
        return Response({'message': 'Appointment cancelled'})

    elif request.method == 'DELETE':
        appointment.delete()
        return Response({'message': 'Appointment deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notification_list_api(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)

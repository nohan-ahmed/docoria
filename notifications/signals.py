from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# local modules
from appointments.models import Appointment
from .models import AppointmentNotification


@receiver(post_save, sender=Appointment)
def create_notification(sender, instance, created, **kwargs):
    if created:
        # Assuming instance has patient, doctor, and hospital attributes
        patient = instance.patient
        doctor = instance.doctor
        hospital = instance.hospital
        
        message = f'{patient.name} has booked an appointment with Dr. {doctor.name} at {hospital.name}.'

        # Create notifications for the hospital and doctor
        AppointmentNotification.objects.create(
            appointment=instance,
            notification_type="appointment_booked",
            message=message,
        )
        
        # Notify doctor
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'doctor_{doctor.id}',
            {
                'type': 'send_notification',
                'message': message,
            }
        )
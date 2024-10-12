from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# local modules
from appointments.models import Appointment
from .models import AppointmentNotification


@receiver(post_save, sender=Appointment)
def notify_on_appointment_creation(sender, instance, created, **kwargs):
    if created:
        # Assuming instance has patient, doctor, and hospital attributes
        patient = instance.patient
        doctor = instance.doctor
        hospital = instance.hospital

        message = f"{patient.user.username} has booked an appointment with Dr. {doctor.user.username} at {hospital.name}."
        print(message, "...")
        # Create notifications for the hospital and doctor
        AppointmentNotification.objects.create(
            appointment=instance,
            notification_type="appointment_booked",
            message=message,
        )

        # Notify doctor
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user_{doctor.user.id}",
            {
                "type": "send_notification",
                "message": message,
            },
        )



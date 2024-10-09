from django.db import models
from appointments.models import Appointment  # Assuming Appointment already links to Patient, Doctor, Hospital
from django.utils import timezone
from .constraints import APPOINTMENT_NOTIFICATION_TYPES

class AppointmentNotification(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=50, choices=APPOINTMENT_NOTIFICATION_TYPES)
    message = models.TextField()  # The content of the notification
    is_read = models.BooleanField(default=False, db_index=True)  # Track whether the notification has been read with index
    read_at = models.DateTimeField(null=True, blank=True)  # Timestamp for when the notification was read
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the notification was created

    class Meta:
        ordering = ['-created_at']  # Order notifications by the most recent

    def __str__(self):
        return f'[{self.get_notification_type_display()}] Notification for Appointment ID: {self.appointment.id}'
    
    def mark_as_read(self):
        """Mark the notification as read."""
        self.is_read = True
        self.read_at = timezone.now()
        self.save()

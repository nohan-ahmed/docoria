from rest_framework import serializers
from . import models

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = ('id', 'doctor', 'patient', 'hospital', 'appointment_type', 'symptom', 'status', 'created_at')
        read_only_fields = ['patient', 'created_at']
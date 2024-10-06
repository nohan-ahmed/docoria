from django.db import models
# local
from doctors.models import Doctor
from patients.models import Patient
from hospitals.models import Hospital
from .constraints import APPOINTMENT_TYPE, STATUS

# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey(to=Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE, related_name='appointments')
    hospital = models.ForeignKey(to=Hospital, on_delete=models.CASCADE, related_name='appointments')
    appointment_type = models.CharField(choices=APPOINTMENT_TYPE, max_length=50, default='offline')
    symptom = models.CharField(max_length=300)
    status = models.CharField(choices=STATUS, max_length=300, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.patient} - {self.doctor} - {self.status}'
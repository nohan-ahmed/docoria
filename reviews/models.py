from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from hospitals.models import Hospital
from .constraints import RATING_CHOICES
# Create your models here.
class Review(models.Model):
    patient = models.ForeignKey(to=Patient, related_name='reviews', on_delete=models.CASCADE)
    doctor = models.ForeignKey(to=Doctor, related_name='reviews', on_delete=models.CASCADE)
    hospital = models.ForeignKey(to=Hospital, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.patient} - {self.doctor} - {self.rating}'
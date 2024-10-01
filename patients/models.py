from django.db import models
from accounts.models import User
from .constraints import BLOOD_GROUP_CHOICES


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient")
    contact_number = models.CharField(max_length=17)
    blood_type = models.CharField(choices=BLOOD_GROUP_CHOICES, max_length=3)
    insurance_provider = models.CharField(max_length=250, null=True, blank=True)
    insurance_number = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
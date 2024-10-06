from django.db import models
# local
from core.utils import user_directory_path
from doctors.models import Doctor
from staffs.models import Staff
from hospitals.models import Hospital
from services.models import Service

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    hospital = models.ForeignKey(to=Hospital, on_delete=models.CASCADE , related_name='departments')
    doctors = models.ManyToManyField(to=Doctor, related_name='departments', null=True, blank=True)
    staffs = models.ManyToManyField(to=Staff, related_name='departments', null=True, blank=True)
    services = models.ManyToManyField(to=Service, related_name='departments')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
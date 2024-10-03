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
    slug = models.SlugField(null=True, blank=True)
    hospital = models.ForeignKey(to=Hospital, on_delete=models.CASCADE , related_name='departments')
    doctors = models.ManyToManyField(to=Doctor, related_name='departments')
    staffs = models.ManyToManyField(to=Staff, related_name='departments')
    services = models.ManyToManyField(to=Service, related_name='departments')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
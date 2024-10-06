from django.db import models
# local
from core.utils import user_directory_path
from doctors.models import Specialization
from hospitals.models import Hospital
# Create your models here.

class Service(models.Model):
    hospital = models.ForeignKey(to=Hospital, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)  # Adjust as needed
    duration = models.DurationField()  # Or you can use IntegerField
    is_available = models.BooleanField(default=True)
    # Optional: Link to a Specialization
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# To store multiple images for a single Service
class ServiceImage(models.Model):
    service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) # TODO: Remove null, blank
    def __str__(self):
        return f'Image for {self.post.title}'
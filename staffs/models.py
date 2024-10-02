from django.db import models
from accounts.models import User
# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff")
    job_title = models.CharField(max_length=250)
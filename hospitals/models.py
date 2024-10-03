from django.db import models
# local
from core.utils import user_directory_path
from accounts.models import User
from doctors.models import Specialization, Doctor
from staffs.models import Staff
from core.models import Country

# Create your models here.


class Hospital(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE , related_name='hospitals')
    name = models.CharField(max_length=100, unique=True)
    slug =models.SlugField(max_length=110, unique=True)
    cover_img = models.ImageField(upload_to=user_directory_path, default='') # Todo: 
    profile_img = models.ImageField(upload_to=user_directory_path, default='') # Todo: 
    description = models.TextField(null=True, blank=True) # Store HTML content
    contact_email = models.EmailField(max_length=254)
    contact_number = models.CharField( max_length=17)
    opening_hours = models.CharField(max_length=300)
    specialties = models.ForeignKey(to=Specialization, on_delete=models.CASCADE)
    doctors = models.ManyToManyField(to=Doctor, related_name='hospitals')
    staffs = models.ManyToManyField(to=Staff, related_name='hospitals')
    created_at = models.DateTimeField( auto_now_add=False)
    
    def __str__(self) -> str:
        return self.name
    
class Location(models.Model):
    hospital = models.ForeignKey(to=Hospital, on_delete=models.CASCADE , related_name='locations')
    country = models.OneToOneField(to=Country, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    zip_code = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=False)
    
    def __str__(self) -> str:
        return f'{self.country} - {self.street_address} - {self.zip_code}'



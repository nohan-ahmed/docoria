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
    cover_img = models.ImageField(upload_to=user_directory_path, null=True, blank=True) # TODO: 
    profile_img = models.ImageField(upload_to=user_directory_path, null=True, blank=True) # TODO: 
    description = models.TextField(null=True, blank=True) # Store HTML content
    contact_email = models.EmailField(max_length=254)
    contact_number = models.CharField( max_length=17)
    opening_hours = models.CharField(max_length=300)
    specialties = models.ManyToManyField(to=Specialization)
    doctors = models.ManyToManyField(to=Doctor, blank=True)
    staffs = models.ManyToManyField(to=Staff, related_name='hospitals', blank=True)
    created_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
class Location(models.Model):
    hospital = models.ForeignKey(to=Hospital, on_delete=models.CASCADE , related_name='locations')
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, null=True, blank=True) #TODO: REMOVE NULL, BLANK
    street_address = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    zip_code = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.country} - {self.street_address} - {self.zip_code}'


class AddDoctorRequest(models.Model):
    from_hospital = models.ForeignKey(Hospital, related_name='sent_add_doctor_requests', on_delete=models.CASCADE)
    to_doctor = models.ForeignKey(Doctor, related_name='received_job_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=(('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')), default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_hospital', 'to_doctor')

    def __str__(self):
        return f'{self.from_hospital} -> {self.to_doctor} ({self.status})'


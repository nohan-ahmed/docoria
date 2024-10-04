from django.db import models
from django.contrib.auth.models import AbstractUser

# Import from DRF

# Local modules
from .constraints import GENDER
from .Managers import Manager
from core.utils import user_directory_path
from core.models import Country
# Create your models here.


class User(AbstractUser):
    # Those are extra fields for custom user model
    profile_image = models.ImageField(upload_to=user_directory_path, null=True, blank=True) 
    cover_image = models.ImageField(upload_to=user_directory_path, null=True, blank=True) 
    gender = models.CharField(choices=GENDER, max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=17, blank=True, null=True)  # 17 characters max
    bio = models.TextField(blank=True, null=True)

    USERNAME_FIELD = "email"  # this field will use to authenticate the user.
    REQUIRED_FIELDS = [
        "username"
    ]  # this field will be required when creating a new user.

    objects = Manager()

    def __str__(self):
        return self.username

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'
        
    def __str__(self) -> str:
        return f"{self.user.username} - country: {self.country}, city: {self.city}"
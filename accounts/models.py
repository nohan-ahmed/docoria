from django.db import models
from django.contrib.auth.models import AbstractUser

# Import from DRF

# Local modules
from .constraints import GENDER
from .Managers import Manager

# Create your models here.


class User(AbstractUser):
    # Those are extra fields for custom user model
    profile_image = models.ImageField(upload_to=None)  # Todo:
    cover_image = models.ImageField(upload_to=None)  # Todo:
    gender = models.CharField(choices=GENDER, max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=17, blank=True, null=True
    )  # 17 characters max
    bio = models.TextField()

    USERNAME_FIELD = "email"  # this field will use to authenticate the user.
    REQUIRED_FIELDS = [
        "username"
    ]  # this field will be required when creating a new user.

    objects = Manager()

    def __str__(self):
        return self.username

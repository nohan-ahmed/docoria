from django.db import models

# Create your models here.

class Country(models.Model):
    iso_code = models.CharField(max_length=2, unique=True)  # ISO 3166-1 alpha-2 code
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=10, blank=True, null=True)  # Optional: add fields like currency
    phone_code = models.CharField(max_length=10, blank=True, null=True)  # Optional: country phone code
    region = models.CharField(max_length=100, blank=True, null=True)  # Optional: world region (e.g., Europe)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
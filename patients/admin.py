from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "contact_number", "blood_type")
    search_fields = ("id", "user", "contact_number", "blood_type")
    list_filter = ("blood_type",)
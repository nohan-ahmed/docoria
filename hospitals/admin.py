from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "user",
        "contact_email",
        "contact_number",
        "opening_hours",
    )
    search_fields = ("id", "name", "contact_email", "contact_number")


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "hospital", "country", "street_address", "city", "zip_code")
    list_filter = ("country", "city", "zip_code")
    search_fields = ("id", "hospital", "country", "street_address", "city", "zip_code")

@admin.register(models.AddDoctorRequest)
class AddDoctorRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "to_doctor", "status", "created_at")
    
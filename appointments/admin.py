from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "doctor", "hospital", "status", "created_at")
    list_filter = ("hospital", "doctor", "patient", "status")
    search_fields = ("id", "patient", "doctor", "hospital", "status", "created_at")

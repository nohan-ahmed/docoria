from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "iso_code", "name", "currency", "phone_code", "region")
    search_fields = ("id", "iso_code", "name", "currency", "phone_code", "region")

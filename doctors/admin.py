from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Specialization)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("id", "name")
    prepopulated_fields = {'slug':['name']}
    
@admin.register(models.Doctor)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", 'experience')
    search_fields = ("id", "user", 'experience')
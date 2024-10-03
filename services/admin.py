from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "hospital", "name", "duration", "price", "is_available")
    search_fields =  ("id", "hospital", "name", "duration", "price", "is_available")
    list_filter = ('is_available',)
    
@admin.register(models.ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ("id", "service", 'created_at')
    search_fields =  ("id", "service")

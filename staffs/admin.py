from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "job_title",)
    list_filter = ("job_title",)
    search_fields = ("id", "user", "job_title")

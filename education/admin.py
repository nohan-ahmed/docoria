from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'country', 'institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'gpa', 'created_at')
    list_filter = ('country', 'institution', 'degree', 'field_of_study', 'gpa', 'created_at')

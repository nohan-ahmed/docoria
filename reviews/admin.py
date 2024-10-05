from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "doctor", "hospital", "rating", "created_at")
    search_fields = ("id", "patient", "doctor", "hospital", "rating", "created_at")
    list_filter = ("hospital", "rating", "created_at")

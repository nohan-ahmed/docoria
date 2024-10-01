from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
    )
    list_filter = ("is_active", "is_staff", "is_superuser", "date_joined", "gender")
    search_fields = ("id", "username", "email", "first_name", "last_name")

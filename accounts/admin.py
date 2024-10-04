from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm  # Use your custom change form
    add_form = CustomUserCreationForm  # Use custom creation form for adding new users

    list_display = ("id", "username", "email", "is_active", "is_staff", "is_superuser")
    list_filter = ("is_active", "is_staff", "is_superuser")

    # Define fieldsets for changing user info
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "profile_image", "cover_image", "gender")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Define fieldsets for adding new users
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "is_active", "is_staff"),
        }),
    )

    search_fields = ("username", "email")
    ordering = ("email",)

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "country", "city", "state", "zip_code")
    list_filter = ("country", "state", "city")
    search_fields = ("id", "user", "country", "city", "state", "zip_code")

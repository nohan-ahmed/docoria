from django.contrib.auth.models import BaseUserManager


class Manager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        
        user = self.model(
            email=self.normalize_email(email), username=username, **extra_fields
        )
        user.set_password(password) # Set encrypted password. 
        user.save(using=self._db) # Save this user to the database
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, username, password, **extra_fields)

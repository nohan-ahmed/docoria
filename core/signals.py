from django.db.models.signals import post_save
from django.dispatch import receiver
# Local modules
from accounts.models import User
from patients.models import Patient

# A receiver function that is triggered after a User object is saved
@receiver(post_save, sender=User)
def create_patient(sender, instance, created, **kwargs):
    # Check if the User instance was just created or not.
    if created:
        # Create a new Patient account for the User
        Patient.objects.create(user=instance)


# =================================================
# Notes:- for django signals
# =================================================
# pre_save and post_save: Triggered before or after a model instance is saved.
# pre_delete and post_delete: Triggered before or after a model instance is deleted.
# Yes, you need to ensure that your Django signal is properly registered in your apps.py file's ready()
# -------------------------------------------------
# sender হলো সেই model জার কনো instance কে save() করলে আমদের receiver function টা triggered হবে। অ্যান্ড instance হলো সে যাকে save() করা হয়েছে।

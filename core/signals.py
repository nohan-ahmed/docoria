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



from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models



@receiver(post_save, sender=models.Hospital)
def create_user(sender, instance, created, **kwargs):
    if created:
        models.Location.objects.create(hospital=instance)
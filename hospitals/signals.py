from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models
from core.models import Country


@receiver(post_save, sender=models.Hospital)
def create_user(sender, instance, created, **kwargs):
    if created:
        models.Location.objects.create(hospital=instance, country=Country.objects.first())
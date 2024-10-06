from django.db.models.signals import post_save
from django.dispatch import receiver
# Local moduels
from . import models
from core.models import Country

@receiver(post_save, sender=models.User)
def create_address(sender, instance, created, **kwargs):
    if created:
        models.Address.objects.create(user=instance, country=Country.objects.first())
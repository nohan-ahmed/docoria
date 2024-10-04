from rest_framework import serializers
from . import models

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hospital
        fields = ('id', 'user', 'name', 'cover_img', 'profile_img', 'description', 'contact_email', 'contact_number', 'opening_hours', 'specialties', 'created_at')
        read_only_fields = ['user']
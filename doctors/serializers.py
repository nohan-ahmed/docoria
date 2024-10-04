from rest_framework import serializers
from . import models

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = ('id', 'user', 'specialization', 'experience', 'created_at')
        read_only_fields = ['user']
        
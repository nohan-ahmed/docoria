from rest_framework import serializers
from . import models

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = ('id', 'user', 'specialization', 'experience', 'created_at')
        read_only_fields = ['user', 'created_at']
        

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = ('id', 'name', 'slug', 'created_at')
        read_only_fields = ['created_at']
        
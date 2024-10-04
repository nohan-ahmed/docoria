from rest_framework import serializers
from . import models

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ('id', 'user', 'contact_number', 'blood_type', 'insurance_provider', 'insurance_number', 'created_at')
        read_only_fields = ['user']
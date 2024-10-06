from rest_framework import serializers
from . import models

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = ['id','hospital','name','description', 'price', 'duration', 'is_available','specialization', 'created_at']
        read_only_fields = ['hospital', 'created_at']
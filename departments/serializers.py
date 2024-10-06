from rest_framework import serializers
from . import models

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ('id', 'name', 'hospital', 'doctors', 'staffs', 'services', 'created_at')
        read_only_fields = ['hospital', 'created_at']
        

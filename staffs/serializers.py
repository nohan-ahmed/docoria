from rest_framework import serializers
from . import models


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = ('id', 'user','job_title', 'created_at')
        read_only_fields = ['user', 'created_at']
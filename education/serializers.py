from rest_framework import serializers
from . import models

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = ('id', 'user', 'country', 'institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'gpa', 'created_at')
        read_only_fields = ['user']
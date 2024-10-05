from rest_framework import serializers
from . import models

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ('id', 'patient', 'doctor', 'hospital', 'rating', 'comment', 'created_at')
        read_only_fields = ['patient', 'created_at']
from rest_framework import serializers
from . import models

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hospital
        fields = ('id', 'user', 'name', 'cover_img', 'profile_img', 'description', 'contact_email', 'contact_number', 'opening_hours', 'specialties','doctors','staffs', 'created_at')
        read_only_fields = ['user']
        extra_kwargs = {
            'doctors': {'required': False},  # Doctors field is optional
            'staffs': {'required': False},  # Staffs field is optional
        }
        
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('id', 'hospital', 'country', 'street_address', 'city', 'zip_code', 'created_at')
        read_only_fields = ['hospital']


class AddDoctorRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AddDoctorRequest
        fields = ['id', 'from_hospital', "to_doctor", 'status', 'created_at']
        read_only_fields = ['from_hospital', 'created_at']
        
    def validate_to_doctor(self, value):
        if models.AddDoctorRequest.objects.filter(to_doctor=value).exists():
            raise serializers.ValidationError("You have already sent a request to this doctor.")
        return value
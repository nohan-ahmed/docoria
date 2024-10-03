from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from . import models


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True, required=True)
    
    class Meta:
        model = models.User
        fields = ('username', 'first_name','last_name', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate(self, attrs):
        password = attrs.get('password')
        # We removed the Confirm Password field as we used this field for validation purposes
        confirm_password = attrs.pop('confirm_password')
        
        # Check that the password and confirm_password match.
        if password != confirm_password:
            raise serializers.ValidationError("Password and confirm password doesn't match!")
        
        try:
            validate_password(password=password, user=None)
        except ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        
        return attrs
    
    def create(self, validated_data):
        # We pop out this password field and store its value in the password variable because we set the password using the set_password method.
        password = validated_data.pop('password')
        user = models.User(**validated_data) # Create an user.
        user.set_password(password) # This method ensures that the password will be stored encrypted.
        user.save()
        return user
    

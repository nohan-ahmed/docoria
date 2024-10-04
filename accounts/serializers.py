from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from . import models

# TODO: Add more fields
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
        user.is_active = False # When a user creates a new account it will be disabled by default.
        user.set_password(password) # This method ensures that the password will be stored encrypted.
        user.save()
        return user
    
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    new_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect")
        return value
    
    def validate(self, attrs):
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')
        
        # Check that the password and confirm_password match.
        if new_password != confirm_password:
            raise serializers.ValidationError("new_password and confirm password doesn't match!")
        
        try:
            validate_password(password=new_password, user=None)
        except ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        
        return attrs
    
    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data.get('new_password'))
        user.save()
        return user
    
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    def validate_email(self, value):
        if not models.User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist")
        return value

class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    def validate(self, attrs):
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')
        
        # Check that the password and confirm_password match.
        if new_password != confirm_password:
            raise serializers.ValidationError("new_password and confirm password doesn't match!")
        
        try:
            validate_password(password=new_password, user=None)
        except ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        
        return attrs
    
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','profile_image', 'cover_image', 'username', 'first_name', 'last_name', 'email', 'gender')
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, smart_str
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags
from itertools import chain
# Import form django rest framework
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Local modules
from . import models
from . import serializers
from .utils import get_tokens_for_user
from .permissions import IsOwnerOrReadOnly
from core.permissions import IsOwnerOrReadOnly as IsOwnerOrReadOnlyForAddress
# Create your views here.


class RegisterAPIView(APIView):
    def post(self, request, format=None):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate a user confirmation token
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Create user verification link 
            verification_link  = f"{request.build_absolute_uri('/api-user/verify-email/')}{uid}/{token}/"

            # Render the HTML template with context
            message = render_to_string("core/verification_mail.html",{
                    "user": user,
                    "verification_link": verification_link,
                },
            )

            # Send the email
            subject = "Email Verification"
            send_mail(subject, strip_tags(message), settings.DEFAULT_FROM_EMAIL, [user.email])
            return Response({'message':"Registration successfully please confirm your email"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VerifyEmailAPIView(APIView):
    def get(self, request, uid, token, format=None):
        try:
            user_id = smart_str(urlsafe_base64_decode(uid))
            user = models.User.objects.get(pk=user_id)
        except Exception:
            user = None
            
        # validate the user & token
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active=True
            user.save()
            token = get_tokens_for_user(user)
            return Response(token, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid verification link.'}, status=status.HTTP_400_BAD_REQUEST)
        
class PasswordChangeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = serializers.PasswordChangeSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            user = serializer.save()
            
            # send password change email
            message = render_to_string('core/change_password_email.html', {
                    'user':user,
                    'time':{timezone.now().strftime('%Y-%m-%d %H:%M:%S')}
                })

            subject = "Your Password Has Been Changed"
            send_mail(subject, strip_tags(message), settings.DEFAULT_FROM_EMAIL, [request.user.email])
            return Response({'Message':'Passwrod changed successfully!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetRequestAPIView(APIView):
    def post(self, request, format=None):
        serializer = serializers.PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = models.User.objects.get(email=serializer.validated_data['email'])

            # Generate a password reset token
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Create password reset link 
            password_reset_link  = f"{request.build_absolute_uri('/api-user/password-reset/')}{uid}/{token}/"

            # Render the HTML template with context
            message = render_to_string("core/password_reset_mail.html",{
                    "user": user,
                    "password_reset_link": password_reset_link,
                },
            )

            # Send the email
            subject = "Password Reset"
            send_mail(subject, strip_tags(message), settings.DEFAULT_FROM_EMAIL, [user.email])
            return Response({"message": "Password reset email has been sent."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetAPIView(APIView):
    def post(self, request, uid, token, format=None):
        try:
            user_id = smart_str(urlsafe_base64_decode(uid))
            user = models.User.objects.get(pk=user_id)
        except Exception:
            user = None
            
        # validate the user & token
        if user is not None and default_token_generator.check_token(user, token):
            serializer = serializers.PasswordResetSerializer(data=request.data, context={'request':request})
            if serializer.is_valid():
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Invalid password reset link."}, status=status.HTTP_400_BAD_REQUEST)

class UserAPIView(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

class AddressAPIView(ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes= [IsOwnerOrReadOnlyForAddress]
    def perform_create(self, serializer):
        """
        perform_create Method: This method is a hook provided by Django REST Framework's ModelViewSet. 
        It allows you to customize the creation of a model instance without completely overriding the create method.
        """
        
        """
        Setting the author: By calling serializer.save(author=self.request.user), you automatically set the author field to the currently authenticated user when a post is created.
        This ensures that the author is set correctly and prevents users from tampering with the field
        """
        serializer.save(user=self.request.user)
        # Thsi method returns None
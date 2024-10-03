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
from rest_framework.response import Response
from rest_framework import status

# Local modules
from . import models
from . import serializers
from .utils import get_tokens_for_user
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
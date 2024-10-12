import os
import django
import jwt
from channels.db import database_sync_to_async
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import DecodeError
from urllib.parse import parse_qs

# Initialize Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "docoria_backend.settings")  # Replace with your actual settings path
django.setup()  # Setup Django environment

User = get_user_model()

@database_sync_to_async
def get_user_from_token(token):
    try:
        # Validate and decode the token
        UntypedToken(token)  # Validate the token structure
        decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_data.get('user_id')

        # Return the authenticated user if the token is valid
        return User.objects.get(id=user_id)
    except (jwt.ExpiredSignatureError, InvalidToken, TokenError, User.DoesNotExist, DecodeError) as e:
        print(f"Token validation error: {str(e)}")  # Add logging for debugging
        return None

class JWTAuthMiddleware:
    """
    Custom middleware for JWT authentication in WebSocket connections.
    """
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        # Extract token from query string
        query_string = parse_qs(scope['query_string'].decode())
        token = query_string.get('token', [None])[0]  # Safely get the token
        
        # If token exists, authenticate user
        if token:
            scope['user'] = await get_user_from_token(token)
        else:
            scope['user'] = None

        # Continue to the inner application (i.e., WebSocket consumer)
        return await self.inner(scope, receive, send)

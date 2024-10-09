"""
ASGI config for docoria_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import notifications.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "docoria_backend.settings")
application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        "websocket":
        AuthMiddlewareStack(
            URLRouter(
                notifications.routing.websocket_urlpatterns,
            )
        ),
    })

"""
ASGI config for recoback project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from ws.tracking import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recoback.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(routing.url_patterns),
})

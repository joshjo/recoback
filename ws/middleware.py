from django.contrib.auth.models import User, AnonymousUser
from channels.db import database_sync_to_async

from rest_framework.authtoken.models import Token
from ws.utils import get_token_from_headers


async def get_user(key: str) -> User | None:
    if not key:
        return AnonymousUser()
    token = await Token.objects.select_related("user").filter(key=key).afirst()
    if not token:
        return AnonymousUser()
    return token.user


class TokenAuthMiddleware:
    """
    Token middleware
    """

    def __init__(self, app) -> None:
        # Store the ASGI application we were passed
        self.app = app

    async def __call__(self, scope, receive, send):
        key = get_token_from_headers(scope["headers"])
        user = await get_user(key)
        scope["user"] = user
        return await self.app(scope, receive, send)

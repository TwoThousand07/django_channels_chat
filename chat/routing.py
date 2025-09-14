from django.urls import path

from . import consumers

websocket_urlspatterns = [
    path('', consumers.JoinAndLeave.as_asgi()),
]
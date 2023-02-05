from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from chat import consumers



websocket_urlpatterns = [
     re_path( r"ws/chat/(?P<chat_box_name>\w+)", consumers.ChatRoomConsumer.as_asgi()),
]



application = application = ProtocolTypeRouter( 
    {
        
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)
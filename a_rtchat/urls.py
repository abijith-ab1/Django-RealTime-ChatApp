from django.urls import path
from .views import *

urlpatterns = [
    path('', chat_view, name="home"),
    path('chat/<str:username>', get_or_create_chatroom, name="start-chat"),
    path('chat/room/<str:chatroom_name>', chat_view, name="chatroom"),
]


from django.urls import path
from .views import *

urlpatterns = [
    path('', chat_view, name="home"),
    path('chat/<str:username>', get_or_create_chatroom, name="start-chat"),
    path('chat/room/<str:chatroom_name>', chat_view, name="chatroom"),
    path('chat/new_groupchat/', create_groupchat, name="new-groupchat"),
    path('chat/edit/<str:chatroom_name>', chatroom_edit_view, name="edit-chatroom"),
    path('chat/delete/<str:chatroom_name>', chatroom_delete_view, name="chatroom-delete"),
    path('chat/leave/<str:chatroom_name>', chatroom_leave_view, name="chatroom-leave"),
    path('chat/fileupload/<str:chatroom_name>', chat_file_upload, name='chat-file-upload'),
]


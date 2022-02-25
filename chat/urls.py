from django.urls import path
from . import views

app_name='chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('room/', views.room, name='room'),
    path('room_message/user_id=<int:pk>/send_message',views.room_message,name='room_message'),
    path('ajax/<int:pk>/loads',views.ajax_load_messages,name='ajax_load_messages'),
    
]
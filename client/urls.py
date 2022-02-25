from django.urls import path
from . import views
app_name='client'
urlpatterns=[
    path('', views.clientform, name='clientform'),
    path('table_client', views.tClients, name='table_client'),

]
from django.urls import include, path
from . import views

app_name = 'CSA'

urlpatterns = [
    path('', views.expediton, name='expedition')

]
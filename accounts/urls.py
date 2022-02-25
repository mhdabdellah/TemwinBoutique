from django.urls import include, path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', views.loginPage, name='logout'),
    path('login/', views.logoutUser, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    # path('user_update/<int:id>/update', views.user_update, name='user_update')

]


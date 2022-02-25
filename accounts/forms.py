from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from .models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','is_staff', 'password1', 'password2']
        labels={
            'is_staff':'manager'
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'image','manager']
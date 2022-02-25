from django import forms
from .models import *

class NewClient(forms.ModelForm):
    class Meta:
        model = Client
        fields ='__all__'  
        exclude =['user','img']
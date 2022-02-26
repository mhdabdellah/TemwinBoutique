from django import forms
from .models import *

class NewClient(forms.ModelForm):
    class Meta:
        model = Client
        fields ='__all__'  
        exclude =['user','qrCode']
    def __init__(self, *args, **kwargs):
        super(NewClient, self).__init__(*args, **kwargs)
        self.fields['email'].required=False 
        self.fields['adresse'].required=False 
        self.fields['tel'].required=False 
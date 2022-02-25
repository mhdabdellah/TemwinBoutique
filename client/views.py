from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from accounts.decorators import admin_and_manager_only
from django.contrib.auth.decorators import login_required
from .forms import NewClient
from django.contrib.auth.models import User
from .models import Client

# Create your views here.

@login_required(login_url='accounts/login')
@admin_and_manager_only
def clientform(request):
    if request.method == 'POST':
        client_Form = NewClient(request.POST)
        if client_Form.is_valid():
            client_Form= client_Form.save(commit=False)
            client_Form.user = User.objects.get(id=request.user.pk)
            client_Form.save()
            messages.success(
                request, f"Felicitations la Client  {client_Form.nom}/{client_Form.prenom} est bien ajoute")
            return redirect(reverse('client:clientform'))
    else:
    
        client_Form = NewClient()
        context={
           
            'client_Form' : client_Form,

        }
        return render(request,'client/clientform.html',context)

@login_required(login_url='accounts/login')
@admin_and_manager_only
def tClients(request):
    context={

        'title': 'les Bénéficiaires',
        'tClients': Client.objects.all()

    }
    return render(request,'client/table_client.html',context)

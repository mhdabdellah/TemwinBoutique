from django.contrib import messages
from django.shortcuts import redirect, render, reverse
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from .decorators import unauthenticated_user, allowed_users, admin_only, admin_and_manager_only
from django.contrib.auth.models import Group


# Create your views here.


# @unauthenticated_user

@admin_and_manager_only
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            us = form.save()
            if us.is_staff:
             group = Group.objects.get(name='manager')
             us.groups.add(group)
             profile=Profile.objects.get(id=us.id)
             print(Profile)
             profile.manager=int(request.user.pk)
             profile.save()
            else:
             group = Group.objects.get(name='shopkipper')
             us.groups.add(group)
             profile=Profile.objects.get(id=us.id)
             profile.manager=int(request.user.pk)
             profile.save()
            messages.success(
                request, f"Felicitation utilisateur bien ajoute f'{us.username}")

            return redirect('stock:table_users')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
           


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html',{'profile': profile})




def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'userform': userform, 'profileform': profileform})


def logoutUser(request):
    logout(request)
    return redirect('stock:home')


    
   
        



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('stock:home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

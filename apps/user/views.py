from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout as auth_logout , login as auth_login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
           auth_login(request, form.get_user())
           return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})



def logout(request):
    auth_logout(request)
    return redirect('home')

def create_groups(sender, **kwargs):
    Group.objects.get_or_create(name='student')
    Group.objects.get_or_create(name='teacher')
    Group.objects.get_or_create(name='admin')
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout as auth_logout , login as auth_login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

def login(request):
    if request.method == 'POST':
        # Procesar el formulario de autenticación si se envió por POST
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
           # Autenticar al usuario y redirigir a la página de inicio si es válido
           auth_login(request, form.get_user())
           return redirect('home')
    else:
        # Mostrar un formulario de autenticación vacío si no se envió por POST
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        # Procesar el formulario de registro si se envió por POST
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Guardar el formulario y redirigir al inicio de sesión si es válido
            form.save()
            return redirect('login')
    else:
        # Mostrar un formulario de registro vacío si no se envió por POST
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def logout(request):
    # Cerrar sesión del usuario y redirigir al inicio
    auth_logout(request)
    return redirect('home')

def create_groups(sender, **kwargs):
    # Crear grupos de usuarios si no existen
    Group.objects.get_or_create(name='student')
    Group.objects.get_or_create(name='teacher')
    Group.objects.get_or_create(name='admin')


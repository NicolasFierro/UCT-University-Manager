from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profesor
from django.contrib.auth.models import Group
from .forms import RegistroProfesorForm, selectorMateriaForm
from ..materias.models import Materia
from .forms import *
from django.shortcuts import render, get_object_or_404

def registro_profesor(request):
    if request.method == 'POST':
        form = RegistroProfesorForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                profesor = form.save(commit=False)
                user = User(username=form.cleaned_data['nombre'], email=form.cleaned_data['email'])
                password = form.cleaned_data['password']
                user.set_password(password)
                user.save()
                profesor.user = user
                profesor.save()
                # Asignar el rol de profesor
                profesor_group, created = Group.objects.get_or_create(name='Profesor')
                user.groups.add(profesor_group)
                # Autenticar y redirigir
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('seleccionar_materias')
                messages.success(request, 'Registro y autenticación exitosos.')
            except IntegrityError:
                messages.error(request, 'Ya existe un usuario con ese nombre de usuario.')
            except Exception as e:
                messages.error(request, f'Error en el registro: {str(e)}')
        else:
            messages.error(request, 'Error en el registro. Por favor revise los datos ingresados.')
    else:
        form = RegistroProfesorForm()
    return render(request, 'profesores/registro_profesor.html', {'form': form})

@login_required
def seleccionar_materias(request):
    if not hasattr(request.user, 'profesor'):
        messages.error(request, 'Solo los profesores pueden acceder a esta página.')
        return redirect('home')

    materias_seleccionadas = []

    if request.method == 'POST':
        form = selectorMateriaForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['seleccionar_todas']:
                materias_seleccionadas = Materia.objects.all()
            else:
                materias_seleccionadas = form.cleaned_data['materias']

            request.user.profesor.materia.set(materias_seleccionadas)
            messages.success(request, 'Materias seleccionadas correctamente.')
        else:
            messages.error(request, 'Error al seleccionar las materias.')
    else:
        form = selectorMateriaForm()

    context = {
        'form': form,
        'materias_seleccionadas': materias_seleccionadas,
    }
    print(materias_seleccionadas)
    return render(request, 'profesores/seleccionar_materias.html', context)

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores/lista_profesores.html', {'profesores': profesores})

def detalles_profesores(request, id):
    # Fetch carrera details by ID or return 404 if not found
    profesores = get_object_or_404(Profesor, id=id)
    # Render the carrera details template with the carrera data
    
    return render(request, 'profesores/profesor_detalle.html', {'profesor_detalle': profesores})

@login_required
def dictar_materia(request, materia_id):
    try:
        materia = Materia.objects.get(id=materia_id)
    except Materia.DoesNotExist:
        messages.error(request, 'La materia no existe.')
        return redirect('home')

    if materia.profesor is not None and materia.profesor != request.user.profesor:
        messages.error(request, f'La materia ya está siendo dictada por {materia.profesor.user.username}.')
        return redirect('home')

    if request.method == 'POST':
        materia.profesor = request.user.profesor
        materia.save()
        messages.success(request, 'Ahora estás dictando la materia.')
        return redirect('home')

    context = {
        'materia': materia,
    }
    return render(request, 'profesores/dictar_materia.html', context)
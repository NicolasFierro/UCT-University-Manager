from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Carreras
from ..estudiantes.models import *
from django.contrib.auth.models import Group
from .forms import InscripcionForm  


def carrerasListas(request):
    # Fetch all carreras from the database
    carreras = Carreras.objects.all()
    # Render the carreras list template with the carreras data
    return render(request, 'carreras/carreras.html', {'carreras': carreras})

def carrerasDetalles(request, id):
    # Fetch carrera details by ID or return 404 if not found
    carrera = get_object_or_404(Carreras, id=id)
    # Render the carrera details template with the carrera data
    
    return render(request, 'carreras/carrerasDetalles.html', {'DetalleCarrera': carrera})


@login_required
def inscripcionCarreras(request, id):
    # Verificar si el usuario pertenece al grupo "profesor"
    if request.user.groups.filter(name='Profesor').exists():
        messages.error(request, 'Los profesores no pueden inscribirse en carreras.')
        return redirect('carreras')  # Redirigir a la lista de carreras o a otra página adecuada

    carrera = get_object_or_404(Carreras, id=id)
    
    # Verificar si el usuario ya está inscrito en alguna carrera
    estudiante_existente = Estudiantes.objects.filter(user=request.user).exists()
    if estudiante_existente:
        messages.error(request, 'Ya estás inscrito en una carrera.')
        return redirect('carreras')  # Redirigir a la lista de carreras o a otra página adecuada

    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            # Guardar los datos en el modelo Estudiantes
            estudiante, created = Estudiantes.objects.get_or_create(user=request.user, carrera=carrera)
            estudiante.nombre = form.cleaned_data['nombre']
            estudiante.apellido = form.cleaned_data['apellido']
            estudiante.email = form.cleaned_data['email']
            estudiante.save()

            # Guardar los datos en el modelo User de Django
            user = request.user
            user.first_name = form.cleaned_data['nombre']
            user.last_name = form.cleaned_data['apellido']
            user.email = form.cleaned_data['email']
            user.save()

            if created:
                estudianteRol, _ = Group.objects.get_or_create(name="estudiante")
                request.user.groups.add(estudianteRol)
            return redirect('carreras')
    else:
        form = InscripcionForm()

    return render(request, 'carreras/inscripcionesCarreras.html', {'form': form, 'carrera': carrera})
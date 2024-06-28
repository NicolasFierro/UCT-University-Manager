from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..carreras.models import * 
from ..estudiantes.models import * 
from .models import *
from .forms import *
from django.contrib import messages

@login_required
def MateriasListas(request):
    try:
        # Obtener el estudiante correspondiente al usuario actual
        estudiante = Estudiantes.objects.get(user=request.user)
        # Filtrar las materias que pertenecen a la carrera del estudiante
        materias = Materia.objects.filter(carreras=estudiante.carrera)
    except Estudiantes.DoesNotExist:
        # Si el estudiante no existe, obtener todas las materias
        materias = Materia.objects.all()

    # Renderizar la plantilla de la lista de materias con los datos de las materias
    return render(request, 'materias/materias.html', {'materias': materias})






@login_required
def inscripcion_materias(request):
    # Verificar si el usuario pertenece al grupo 'estudiante'
    if not request.user.groups.filter(name='estudiante').exists():
        messages.error(request, 'Solo los estudiantes pueden inscribirse en materias.')
        return redirect('materias')  # Redirigir a la lista de materias u otra página apropiada

    try:
        # Obtener el estudiante correspondiente al usuario actual
        estudiante = Estudiantes.objects.get(user=request.user)
    except Estudiantes.DoesNotExist:
        messages.error(request, 'El estudiante no existe.')
        return redirect('materias')  # Redirigir a la lista de materias u otra página apropiada

    if request.method == 'POST':
        # Crear un formulario con los datos POST y la instancia del estudiante y usuario actual
        form = InscripcionMateriasForm(request.POST, instance=estudiante, user=request.user)
        if form.is_valid():
            # Obtener las materias seleccionadas
            materias_seleccionadas = form.cleaned_data['materia']
            # Verificar si ya está inscrito en alguna de las materias seleccionadas
            ya_inscritas = estudiante.materia.filter(id__in=materias_seleccionadas)
            if ya_inscritas.exists():
                messages.error(request, 'Ya estás inscrito en una o más de las materias seleccionadas.')
            else:
                form.save()
                messages.success(request, 'Inscripción de la materia realizada con éxito.')
            return redirect("inscripcion_materias")
        else:
            messages.error(request, 'Error al inscribir la materia.')
    else:
        # Crear un formulario vacío con la instancia del estudiante y usuario actual
        form = InscripcionMateriasForm(instance=estudiante, user=request.user)
    
    # Renderizar la plantilla de inscripción de materias con el formulario
    return render(request, 'materias/inscripcion_materias.html', {'form': form})

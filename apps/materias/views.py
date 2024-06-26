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
        estudiante = Estudiantes.objects.get(user=request.user)
        materias = Materia.objects.filter(carreras=estudiante.carrera)
    except Estudiantes.DoesNotExist:
        materias = Materia.objects.all()

    return render(request, 'materias/materias.html', {'materias': materias})





@login_required
def inscripcion_materias(request):
    # Check if the user belongs to the 'estudiante' group
    if not request.user.groups.filter(name='estudiante').exists():
        messages.error(request, 'Solo los estudiantes pueden inscribirse en materias.')
        return redirect('materias')  # Redirect to the list of subjects or another appropriate page

    try:
        estudiante = Estudiantes.objects.get(user=request.user)
    except Estudiantes.DoesNotExist:
        messages.error(request, 'El estudiante no existe.')
        return redirect('materias')  # Redirect to the list of subjects or another appropriate page

    if request.method == 'POST':
        form = InscripcionMateriasForm(request.POST, instance=estudiante, user=request.user)
        if form.is_valid():
            materias_seleccionadas = form.cleaned_data['materia']
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
        form = InscripcionMateriasForm(instance=estudiante, user=request.user)
    
    return render(request, 'materias/inscripcion_materias.html', {'form': form})
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def carrerasListas(request):
    carreras = Carreras.objects.all()
    return render(request, 'carreras/carreras.html', {'carreras': carreras})

def carrerasDetalles(request, id):
    carrerasDetalles = get_object_or_404(Carreras, id=id)
    return render(request, 'carreras/carrerasDetalles.html', {'carrerasDetalle': carrerasDetalles})
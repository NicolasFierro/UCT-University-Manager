from django.urls import path
from .views import carrerasListas, carrerasDetalles, inscripcionCarreras

urlpatterns = [
    path('carreras/', carrerasListas, name='carreras'),
    path('carreras/<int:id>/', carrerasDetalles, name='carrera_detalle'),
    path('carreras/<int:id>/inscripcion/', inscripcionCarreras, name='inscripcion_carrera'),
]

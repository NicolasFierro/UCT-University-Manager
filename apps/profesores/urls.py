from django.urls import path
from .views import *

urlpatterns = [
    path("postular_profesor/", registro_profesor, name="postular_profesor"),
    path("seleccionar_materias/", seleccionar_materias, name="seleccionar_materias"),
    path('profesor_detalle/<int:id>', detalles_profesores, name='profesor_detalle'),
    path('profesores/', lista_profesores, name='profesores'),
    path('dictar_materia/<int:materia_id>/', dictar_materia, name='dictar_materia'),
]

from django.urls import path
from .views import * 

urlpatterns = [
    path("materias/", MateriasListas, name="materias"),
    path("inscripcion_materias/", inscripcion_materias, name="inscripcion_materias"),
    
    
]

from django.urls import path
from .views import * 

urlpatterns = [
    path('carreras/', carrerasListas, name='carreras' ),
    path('carreras/<int:id>', carrerasDetalles, name = 'carrera detalle' )
]

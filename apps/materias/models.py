from django.db import models
from apps.carreras.models import Carreras


class Materia(models.Model):
    NombreMateria = models.CharField(max_length=100, verbose_name="Nombre de la materia")
    DescripcionMateria = models.TextField(verbose_name="Descripcion de la materia")
    CreacionMateria = models.DateTimeField(auto_now_add=True, verbose_name="creacion de la materia")
    carreras = models.ForeignKey(Carreras, on_delete=models.CASCADE, related_name='Materia')
    
    def __str__(self):
        return self.NombreMateria
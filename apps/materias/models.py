from django.db import models
from django.apps import apps

class Materia(models.Model):
    NombreMateria = models.CharField(max_length=100, verbose_name="Nombre de la materia")
    DescripcionMateria = models.TextField(verbose_name="Descripcion de la materia")
    CreacionMateria = models.DateTimeField(auto_now_add=True, verbose_name="creacion de la materia")
    duraccionMateria = models.CharField(verbose_name="Duracion de la materia", max_length=100)
    carreras = models.ForeignKey(
        'carreras.Carreras', 
        on_delete=models.CASCADE, 
        related_name='Materia'
    )
    imagenesMateria = models.ImageField(upload_to="Materias/")
    profesor = models.ForeignKey(
        'profesores.Profesor', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='Materia_dictadas'
    )

    def __str__(self):
        return self.NombreMateria

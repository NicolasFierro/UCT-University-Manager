from django.db import models


class Carreras(models.Model):
    NombreCarrera = models.CharField(max_length=100, verbose_name="Nombre de la Carrera")
    DescripcionCarrera = models.TextField(verbose_name="Descripcion de la Carrera")
    DuracionCarrera = models.CharField(max_length=100, verbose_name="Duración en Semestres")
    CostoCarrera = models.IntegerField(verbose_name="Créditos")
    creacionCarrera = models.DateTimeField(auto_now_add=True, verbose_name="Creacion de la carrea")


    def __str__(self):
        return f"{self.id} - {self.NombreCarrera}"


# Create your models here.

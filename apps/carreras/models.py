from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Carreras(models.Model):
    NombreCarrera = models.CharField(max_length=100, verbose_name="Nombre de la Carrera")
    DescripcionCarrera = models.TextField(verbose_name="Descripcion de la Carrera", validators=[MinLengthValidator(100), MaxLengthValidator(200)])
    DuracionCarrera = models.CharField(max_length=100, verbose_name="Duración en Semestres")
    CostoCarrera = models.IntegerField(verbose_name="Créditos")
    creacionCarrera = models.DateTimeField(auto_now_add=True, verbose_name="Creacion de la carrea")
    imagenesCarrera = models.ImageField(_("Imagen de la carrera"), upload_to='Carreras/')

    def __str__(self):
        return self.NombreCarrera

   


# Create your models here.

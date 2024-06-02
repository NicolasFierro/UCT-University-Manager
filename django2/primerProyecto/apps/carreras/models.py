from django.db import models


class Careeras(models.Model):
    idClass = models.IntegerField(primary_key=True, verbose_name="ID de Carrera")
    nameClass = models.CharField(max_length=100, verbose_name="Nombre de la Carrera")
    durationClass = models.IntegerField(verbose_name="Duración en Semestres")
    creditClass = models.IntegerField(verbose_name="Créditos")

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        ordering = ['idClass']

    def __str__(self):
        return f"{self.nameClass} (ID: {self.idClass})"
# Create your models here.

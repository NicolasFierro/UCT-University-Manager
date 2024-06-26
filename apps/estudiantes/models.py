from django.db import models

from django.contrib.auth.models import User
from apps.carreras.models import Carreras
from apps.materias.models import Materia


class Estudiantes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="estudiantes")
    carrera = models.ForeignKey(Carreras, on_delete=models.CASCADE, related_name="estudiantes")
    materia = models.ManyToManyField(Materia, related_name="estudiantes")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
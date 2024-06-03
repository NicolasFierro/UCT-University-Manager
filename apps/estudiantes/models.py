from django.db import models

from django.contrib.auth.models import User
from apps.carreras.models import Carreras
from apps.materias.models import Materia


class Estudiantes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    carrera = models.ForeignKey(Carreras, on_delete=models.CASCADE, related_name="carrera")
    materia = models.ManyToManyField(Materia, related_name= "materia")

    def __str__(self):
        return self.user.username
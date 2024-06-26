from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profesor")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    foto = models.ImageField(upload_to='fotos_profesores/', blank=True, null=True)
    especialidad = models.CharField(max_length=100)
    experiencia = models.TextField()
    fecha_postulacion = models.DateTimeField(auto_now_add=True)
    materia = models.ManyToManyField(
        'materias.Materia', 
        related_name="profesores_materias"
    )
    carrera = models.ManyToManyField(
        'carreras.Carreras', 
        related_name="profesores"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

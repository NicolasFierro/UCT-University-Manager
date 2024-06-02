from django.db import models
from datetime import datetime
# Create your models here.
class Article(models.Model):
    userName = models.CharField(max_length=150)
    email = models.EmailField(max_length=200, blank=True, null=True)
    password = models.TextField()
    phone = models.BooleanField()

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

class Category(models.Model):
    userName = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    

class Register(models.Model):
    userName = models.CharField(max_length=150)
    email = models.EmailField(max_length=200),
    password = models.CharField(max_length=30)
    phone = models.IntegerField()

class LoginStudent(models.Model):
    userName = models.CharField(max_length=110)
    password = models.CharField(max_length=30) 

class LoginAdmins(models.Model):
    userName = models.CharField(max_length=110)
    password = models.CharField(max_length=30) 

# class Careers(models.Model):
#     idClass = models.IntegerField(primary_key=True, verbose_name="ID de Carrera")
#     nameClass = models.CharField(max_length=100, verbose_name="Nombre de la Carrera")
#     durationClass = models.IntegerField(verbose_name="Duración en Semestres")
#     creditClass = models.IntegerField(verbose_name="Créditos")

#     class Meta:
#         verbose_name = "Carrera"
#         verbose_name_plural = "Carreras"
#         ordering = ['idClass']

#     def __str__(self):
#         return f"{self.nameClass} (ID: {self.idClass})"

# class Carrera(models.Model):
#     nombre = models.CharField(max_length=255)
#     # Otros campos de la clase Carrera

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    # Otros campos de la clase Profesor

class Materia(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    creditos = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=datetime.now)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    profesores = models.ManyToManyField(Profesor)


from django.contrib import admin
from .models import *

class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'carrera_names')
    search_fields = ('id', 'user__username', 'carrera__NombreCarrera')
    list_filter = ('user__username', 'carrera__NombreCarrera')
    list_display_links = ('id', 'user', 'carrera_names')

    def carrera_names(self, obj):
        return obj.carrera.NombreCarrera if obj.carrera else ""

    carrera_names.short_description = "Carreras"

admin.site.register(Estudiantes, EstudiantesAdmin)
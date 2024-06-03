from django.contrib import admin
from .models import *

class MateriaAdmin(admin.ModelAdmin):
        list_display = ('id', 'NombreMateria', 'carreras', 'CreacionMateria')
        search_fields = ('id', 'NombreMateria')
        list_filter = ('id', 'NombreMateria')
        list_display_links = ('id', 'NombreMateria', 'carreras', 'CreacionMateria')


admin.site.register(Materia, MateriaAdmin)


from django.contrib import admin
from .models import *

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'NombreCarrera', 'DuracionCarrera')
    search_fields = ('id', 'NombreCarrera')
    list_filter = ('id', 'NombreCarrera')
    list_display_links = ('id', 'NombreCarrera', 'DuracionCarrera')

admin.site.register(Carreras, CarreraAdmin)
# Register your models here.

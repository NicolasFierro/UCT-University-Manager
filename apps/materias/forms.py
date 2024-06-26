from django import forms 
from ..estudiantes.models import *
from .models import *

class InscripcionMateriasForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = ['materia']
        widgets = {
            'materia': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(InscripcionMateriasForm, self).__init__(*args, **kwargs)
        estudiante = user.estudiantes
        self.fields['materia'].queryset = Materia.objects.filter(carreras=estudiante.carrera).exclude(estudiantes=estudiante)
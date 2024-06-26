from django import forms
from ..materias.models import Materia
from .models import Profesor
from django.contrib.auth.models import User



from django import forms
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from .models import Profesor  # Ajustar la importación según tu estructura de proyecto

class RegistroProfesorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'foto', 'especialidad']

    def clean_foto(self):
        foto = self.cleaned_data.get('foto', False)
        if not foto:
            raise ValidationError("Este campo es obligatorio.")
        
        try:
            # Intentar obtener las dimensiones de la imagen
            w, h = get_image_dimensions(foto)
            # Si no se puede obtener, lanza una excepción
        except Exception:
            raise ValidationError("El archivo subido no es una imagen válida.")
        
        # Validar el tamaño del archivo si es necesario
        if foto.size > 4 * 1024 * 1024:
            raise ValidationError("El tamaño de la imagen debe ser menor a 4MB.")
        
        return foto

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if User.objects.filter(username=nombre).exists():
            raise forms.ValidationError("Este nombre de usuario ya está registrado.")
        return nombre

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Profesor.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un profesor con este correo electrónico.")
        return email

    def save(self, commit=True):
        profesor = super().save(commit=False)
        user = User(username=self.cleaned_data['nombre'], email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            profesor.user = user
            profesor.save()
        return profesor
        
class selectorMateriaForm(forms.Form):
    materias = forms.ModelMultipleChoiceField(
        queryset=Materia.objects.all(),
        widget = forms.SelectMultiple,
        required = False
    )
    seleccionar_todas = forms.BooleanField(required=False, initial=False, label='Seleccionar todas las materias')
from django import forms 
from django.core import validators
from .models import Careers
from .models import Materia
from .models import Register

class FormArticulo(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el Titulo',
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ]{5,}$', 'El título está mal digitado', 'invalid_title'),

        ]
    )
    content = forms.CharField(
        label="Contenido",
        max_length=40,
        required=False,
        widget= forms.Textarea(
            attrs= {
                'placeholder': 'Ingrese el Contenido',
                'class':'contenido_form_article'
            }
        )
    )

    public_options= [(0,'No'),(1,'Si')]
    public=forms.TypedChoiceField(
        label='¿publicado?',
        choices=public_options)

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class CreateUserForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    lastname = forms.CharField(label='Apellidos')
    email = forms.EmailField(label='Correo electronico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    phone =forms.IntegerField(label='Telefono')

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')

class AgregarCareersForm(forms.ModelForm):
    class Meta:
        models = Careers
        fields = ['idClass', 'nameClass', 'durationClass', 'creditClass']

class AgregarMateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['codigo', 'nombre', 'descripcion', 'creditos', 'carrera', 'profesores']
        widgets = {
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'profesores': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

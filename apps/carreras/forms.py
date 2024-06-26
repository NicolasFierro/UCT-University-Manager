from django import forms

class InscripcionForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    def clean_nombre(self):
        data = self.cleaned_data['nombre']
        if not data:
            raise forms.ValidationError("Este campo es obligatorio.")
        return data

    def clean_apellido(self):
        data = self.cleaned_data['apellido']
        if not data:
            raise forms.ValidationError("Este campo es obligatorio.")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if not data:
            raise forms.ValidationError("Este campo es obligatorio.")
        return data

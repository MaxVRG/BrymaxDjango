from django import forms
from .models import Mantencion

class MantencionForm(forms.ModelForm):
    class Meta:
        model = Mantencion
        fields = ['nombre', 'email', 'telefono', 'tipo_mantencion', 'direccion', 'fecha']
from django import forms
from .models import Contacto
from .models import Mantencion


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 5}),
        }


class MantencionForm(forms.ModelForm):
    class Meta:
        model = Mantencion
        fields = ['nombre', 'email', 'telefono', 'tipo_mantencion', 'direccion', 'fecha']
from django.contrib import admin
from .models import EquipoNuevo, EquipoUsado, Consola

# Register your models here.

admin.site.register(EquipoNuevo)
admin.site.register(EquipoUsado)
admin.site.register(Consola)
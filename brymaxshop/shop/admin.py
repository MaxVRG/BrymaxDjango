from django.contrib import admin
from .models import Producto, ItemCarrito
from .models import Mantencion
from .models import Contacto
# Register your models here.
admin.site.register(Producto)
admin.site.register(ItemCarrito)
admin.site.register(Mantencion)
admin.site.register(Contacto)
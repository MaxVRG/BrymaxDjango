from django.contrib import admin
from .models import Producto, ItemCarrito

# Register your models here.
admin.site.register(Producto)
admin.site.register(ItemCarrito)
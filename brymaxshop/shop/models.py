from django.db import models
from django.contrib.auth.models import User

def product_image_path(instance, filename):
    # Construye la ruta de almacenamiento para la imagen basada en el ID del producto
    return f'productos/{instance.producto_id}/{filename}'

class BaseProducto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    producto_id = models.PositiveIntegerField(primary_key=True)  # Usar 'id' predeterminado es más sencillo

    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True

class EquipoNuevo(BaseProducto):
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to=product_image_path, null=True, blank=True)

class EquipoUsado(BaseProducto):
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to=product_image_path, null=True, blank=True)

class Consola(BaseProducto):
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to=product_image_path, null=True, blank=True)

class Producto(BaseProducto):
    pass

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def subtotal(self):
        return self.producto.precio * self.cantidad

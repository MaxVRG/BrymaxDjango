from django.db import models
from django.contrib.auth.models import User

def product_image_path(instance, filename):
    # Construye la ruta de almacenamiento para la imagen basada en el ID del producto
     return f'media/productos/{instance.producto_id}/{filename}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    producto_id = models.PositiveIntegerField(primary_key=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to=product_image_path, null=True, blank=True)

    def __str__(self):
        return self.nombre

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='items_carrito')
    cantidad = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def subtotal(self):
        return self.producto.precio * self.cantidad


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    


    
class Mantencion(models.Model):
    nombre = models.CharField(max_length=101)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    tipo_mantencion = models.CharField(max_length=20, choices=[('domicilio', 'A domicilio'), ('local', 'En el local')])
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre
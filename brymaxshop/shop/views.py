import logging
from venv import logger
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, ItemCarrito
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactoForm
from .forms import MantencionForm

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def nuevos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'shop/nuevos.html', context)


def usados(request):
    return render(request, 'shop/usados.html')

def mantencion(request):
    return render(request, 'shop/mantencion.html')

def consolas(request):
    return render(request, 'shop/consolas.html')

def info(request):
    return render(request, 'shop/info.html')

def contacto(request):
    return render(request, 'shop/contacto.html')

def carrito(request):
    return render(request, 'shop/carrito.html')



def añadir_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        if cantidad <= 0:
            messages.error(request, 'La cantidad debe ser mayor que cero.')
        elif cantidad > producto.stock:
            messages.error(request, 'No hay suficiente stock disponible.')
        else:
            # Crear o actualizar el ítem del carrito en la base de datos
            item_carrito, created = ItemCarrito.objects.get_or_create(
                producto=producto,
                usuario=request.user,  # Ajusta esto según cómo manejes la autenticación
                defaults={'cantidad': cantidad}
            )

            if not created:
                item_carrito.cantidad += cantidad
                item_carrito.save()

            messages.success(request, f'{producto.nombre} añadido al carrito.')
            return redirect('carrito')  # Redirigir a la vista del carrito

    return redirect('index')  # Redirigir a la página de inicio si no es un POST o si hay errores


def carrito(request):
    # Obtener todos los ítems del carrito para el usuario actual
    items_carrito = ItemCarrito.objects.filter(usuario=request.user)
    
    total = 0
    productos_carrito = []

    # Calcular el total y construir la lista de productos en el carrito
    for item in items_carrito:
        subtotal = item.producto.precio * item.cantidad
        total += subtotal
        productos_carrito.append({
            'id': item.producto.pk,  # Usar pk en lugar de id
            'nombre': item.producto.nombre,
            'precio': item.producto.precio,
            'cantidad': item.cantidad,
            'subtotal': subtotal
        })

    context = {
        'productos_carrito': productos_carrito,
        'total': total,
    }
    return render(request, 'shop/carrito.html', context)


def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    if request.method == 'POST':
        # Buscar el ítem del carrito correspondiente
        item_carrito = get_object_or_404(ItemCarrito, producto=producto, usuario=request.user)
        
        if item_carrito.cantidad > 1:
            # Si hay más de una unidad, reducir la cantidad
            item_carrito.cantidad -= 1
            item_carrito.save()
            messages.success(request, f'Se redujo la cantidad de {producto.nombre} en el carrito.')
        else:
            # Si solo hay una unidad, eliminar el ítem del carrito completamente
            item_carrito.delete()
            messages.success(request, f'Se eliminó {producto.nombre} del carrito.')
    
    return redirect('carrito')


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu mensaje ha sido enviado con éxito!')
            return redirect('contacto')  # Redirige a la misma página
    else:
        form = ContactoForm()
    
    return render(request, 'shop/contacto.html', {'form': form})


def agendar_mantencion(request):
    if request.method == 'POST':
        form = MantencionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Mantención agendada correctamente!')
            return redirect('index')  # Redirige a la página de inicio o donde prefieras
    else:
        form = MantencionForm()
    
    return render(request, 'shop/mantencion.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, ItemCarrito
from django.contrib.auth.decorators import login_required

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
    producto = get_object_or_404(Producto, producto_id=producto_id)

    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        if cantidad <= 0:
            messages.error(request, 'La cantidad debe ser mayor que cero.')
        elif cantidad > producto.stock:
            messages.error(request, 'No hay suficiente stock disponible.')
        else:
            item, created = ItemCarrito.objects.get_or_create(
                producto=producto,
                usuario=request.user,
                defaults={'cantidad': cantidad}
            )
            if not created:
                item.cantidad += cantidad
                item.save()
            messages.success(request, f'{producto.nombre} añadido al carrito.')
            return redirect('carrito')

    return redirect('index')



def carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0
    
    for producto_id, item in carrito.items():
        productos.append({
            'nombre': item['nombre'],
            'precio': item['precio'],
            'cantidad': item['cantidad'],
            'subtotal': float(item['precio']) * item['cantidad'],
        })
        total += float(item['precio']) * item['cantidad']
    
    return render(request, 'shop/carrito.html', {'productos': productos, 'total': total})


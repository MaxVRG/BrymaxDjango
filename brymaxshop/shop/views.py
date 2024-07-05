from django.shortcuts import render, redirect, get_object_or_404
from .models import EquipoNuevo, Producto, ItemCarrito
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def nuevos(request):
    productos = EquipoNuevo.objects.all()
    return render(request, 'shop/nuevos.html', {'productos': productos})


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
        # Asegúrate de que la cantidad sea positiva y el stock sea suficiente
        if cantidad <= 0:
            messages.error(request, 'La cantidad debe ser mayor que cero.')
        elif cantidad > producto.stock:
            messages.error(request, 'No hay suficiente stock disponible.')
        else:
            # Crear o actualizar el item en el carrito del usuario actual
            item, created = ItemCarrito.objects.get_or_create(
                producto=producto,
                usuario=request.user,
                defaults={'cantidad': cantidad}
            )
            if not created:
                item.cantidad += cantidad
                item.save()
            messages.success(request, f'{producto.nombre} añadido al carrito.')
            return redirect('shop/carrito.html')  # Redirige a la página del carrito

    return redirect('shop/index.html')  # Redirige a la página del producto después de añadirlo


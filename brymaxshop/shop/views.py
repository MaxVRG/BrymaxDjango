from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def nuevos(request):
    return render(request, 'shop/nuevos.html')

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
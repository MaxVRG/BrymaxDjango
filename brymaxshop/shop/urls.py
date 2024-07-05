from django.urls import path
from .import views 


urlpatterns = [
    path('', views.index,name="index"),
    path('nuevos/', views.nuevos, name='nuevos'),
    path('usados/', views.usados, name='usados'),
    path('mantencion/', views.mantencion, name='mantencion'),
    path('consolas/', views.consolas, name='consolas'),
    path('info/', views.info, name='info'),
    path('contacto/', views.contacto, name='contacto'),
    path('carrito/', views.carrito, name='carrito'),

    path('añadir/<int:producto_id>/', views.añadir_al_carrito, name='añadir_al_carrito'),
]
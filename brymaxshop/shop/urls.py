from django.urls import path
from .import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,name="index"),
    path('nuevos/', views.nuevos, name='nuevos'),
    path('usados/', views.usados, name='usados'),
    path('mantencion/', views.mantencion, name='mantencion'),
    path('consolas/', views.consolas, name='consolas'),
    path('info/', views.info, name='info'),
    path('contacto/', views.contacto, name='contacto'),
    path('carrito/', views.carrito, name='carrito'),
    path('mantencion/', views.agendar_mantencion, name='agendar_mantencion'),
    path('añadir/<int:producto_id>/', views.añadir_al_carrito, name='añadir_al_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('contacto/', views.contacto, name='contacto'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
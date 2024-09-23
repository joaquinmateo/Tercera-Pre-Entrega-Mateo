from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('crea-producto', crea_producto),
    path('lista-catalogo/', lista_catalago, name = "Catalogo"),
    path('entrega/', pedir, name = "Entrega"),
    path('registro/', registro, name = "Registro"),
    path('buscar-producto/', buscar_producto, name = "BuscarProducto"),
]
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', padre),
    path('inicio/', inicio, name="Inicio"),
    path('lista-catalogo/', CatalogoList.as_view(), name = "Catalogo"),
    path('detalle-catalogo/<pk>', CatalogoDetail.as_view(), name = "DetalleCatalogo"),
    path('entrega/', busqueda_producto, name = "Entrega"),
    path('buscar-producto/', buscar_producto, name = "BuscarProducto"),
    path('login/', login_view, name = "Login"),
    path('registrar/', register, name = "Registro"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name = "Logout"),
    path('editar-perfil/', editar_perfil, name = "EditarPerfil"),
    path('crea-opinion/', crea_opinion, name = "CreaOpinion"),
]
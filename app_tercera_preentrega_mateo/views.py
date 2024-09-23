from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def inicio(req):

    return render(req, "inicio.html", {})

def crea_producto(req, marca, producto, precio):
    nuevo_producto = Catalogo(marca=marca, producto=producto, precio=precio)
    nuevo_producto.save()
    return HttpResponse(f"""
        <p>Marca: {nuevo_producto.marca} - Producto: {nuevo_producto.producto} - Precio: {nuevo_producto.precio}</p>
    """)

def lista_catalago(req):
    lista = Catalogo.objects.all()
    return render(req, "lista_catalogo.html", {"lista_catalogo": lista})

def registro(req):

    return render(req, "registro.html", {})

def pedir(req):

    return render(req, "pedir.html", {})

def buscar_producto(req):

    nom_marca = req.GET["marca"]

    productos = Catalogo.objects.filter(marca__icontains=nom_marca) #Ahora interactua con la base de datos, filter permite trabajar con más de un objeto e icontains hace una busqueda aproximada

    return render(req, "resultado_busqueda.html", { "productos": productos, "marca": nom_marca}) #Creamos el template
    




# Create your views here.

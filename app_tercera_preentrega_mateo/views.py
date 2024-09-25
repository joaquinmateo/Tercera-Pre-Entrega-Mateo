from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

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

    productos = Catalogo.objects.filter(marca__icontains=nom_marca) 

    return render(req, "resultado_busqueda.html", { "productos": productos, "marca": nom_marca}) 
    

def registro(req):

    if req.method == 'POST':

        mi_formulario = formulario(req.POST) 

        if mi_formulario.is_valid(): 

            data = mi_formulario.cleaned_data    

            nuevo_cliente = Cliente(nombre=req.POST["nombre"], apellido=req.POST["apellido"], email=req.POST["email"])
            nuevo_cliente.save()

            return render(req, "inicio.html", {})
        else:   
            return render(req, "registro.html", { "mi_formulario": mi_formulario})
    
    else:

        mi_formulario = formulario()

        return render(req, "registro.html", { "mi_formulario": mi_formulario}) 
    
def dejar_opinion(req):
        if req.method == 'POST':

            mi_critica = critica(req.POST) 

            if mi_critica.is_valid(): 

                data = mi_critica.cleaned_data    

                nueva_critica = Opiniones(opinion=req.POST["opinion"])  
                nueva_critica.save()

                return render(req, "inicio.html", {})
            else:   
                return render(req, "opiniones.html", { "mi_critica": mi_critica})
    
        else:

            mi_critica = critica()

            return render(req, "opiniones.html", { "mi_critica": mi_critica}) 



# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin 

def padre(req):
    return render(req, "padre.html", {})

@login_required
def inicio(req):

    return render(req, "inicio.html", {})

class CatalogoList(LoginRequiredMixin, ListView):
    model = Catalogo
    template_name = 'lista_catalogo.html'
    context_object_name = 'catalogos'

class CatalogoDetail(LoginRequiredMixin, DetailView):
    model=Catalogo
    template_name = 'detalle_catalogo.html'
    context_object_name = 'catalogo'

@login_required
def busqueda_producto(req):

    return render(req, "pedir.html", {})

@login_required
def buscar_producto(req):

    nom_marca = req.GET["marca"]

    productos = Catalogo.objects.filter(marca__icontains=nom_marca) 

    return render(req, "resultado_busqueda.html", { "productos": productos, "marca": nom_marca}) 
    
 
    
def login_view(req):
    if req.method == 'POST':

        mi_formulario = AuthenticationForm(req, data=req.POST)
        
        if mi_formulario.is_valid(): 

            data = mi_formulario.cleaned_data    

            usuario = data['username']
            psw = data['password']

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "inicio.html", { "mensaje": f"Bienvenido {usuario}"})
            else:
                return render(req, "padre.html", { "mensaje": f"Datos incorretos!"})
            
        
        else:   
            
            return render(req, "login.html", { "mi_formulario": mi_formulario }) 
             

    else:

        mi_formulario = AuthenticationForm()
        
        return render(req, "login.html", { "mi_formulario": mi_formulario }) 

def register(req):
    if req.method == 'POST':

        mi_formulario = UserCreationForm(req.POST)
        
        if mi_formulario.is_valid(): 

            data = mi_formulario.cleaned_data    

            usuario = data['username']

            mi_formulario.save()

            return render(req, "inicio.html", { "mensaje": f"El usuario {usuario} fue creado exitosamente!"})
            
        else:
            return render(req, "registro.html", { "mi_formulario": mi_formulario }) 
   
    else:

        mi_formulario = UserCreationForm()
        
        return render(req, "registro.html", { "mi_formulario": mi_formulario }) 
    
      
@login_required
def editar_perfil(req):
    
    usuario = req.user
    
    if req.method == 'POST':
        
        mi_formulario= UserEditForm(req.POST, instance=req.user)

        if mi_formulario.is_valid(): 

            data = mi_formulario.cleaned_data    

            usuario.username = data['username']
            usuario.password = data['password']
            usuario.set_password(data["password1"])

            usuario.save()

            return render(req, "inicio.html", { "mensaje": f"Datos actualizados exitosamente!"})
            
        else:
            return render(req, "editar_perfil.html", { "mi_formulario": mi_formulario }) 
    else:
            mi_formulario = UserEditForm()
            return render(req, "editar_perfil.html", {"mi_formulario": mi_formulario}) 
    

@login_required       
def crea_opinion(req):

    if req.method == 'POST':

        mi_formulario = OpinionFormulario(req.POST)

        if mi_formulario.is_valid(): 

            data = mi_formulario.cleaned_data    

            nueva_opinion = Opiniones(opinion=req.POST["opinion"], email=req.POST["email"])
            nueva_opinion.save()

            return render(req, "inicio.html", { "mensaje": f"Su mensaje ha sido enviado, pronto nos comunicaremos!"})
        else:   
            return render(req, "opinion_create.html", { "mi_formulario": mi_formulario})
    
    else:

        mi_formulario = OpinionFormulario()
        return render(req, "opinion_create.html", { "mi_formulario": mi_formulario})
    

# Create your views here.

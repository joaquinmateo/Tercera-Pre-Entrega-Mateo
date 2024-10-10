from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

class Catalogo(models.Model):
    marca = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True)  
    def __str__(self) -> str:
        return f'{self.marca} - {self.producto} - ${self.precio}'
    
    def mostrar_imagen(self):
        if self.imagen:
            return format_html('<img src= "{}" width="100" height="100" />'.format(self.imagen.url))
        else:
            return ''
        
    mostrar_imagen.short_description = "Imagen"
    
class Opiniones(models.Model):
    email = models.EmailField(unique=True)
    opinion = models.CharField(max_length=250)
    def __str__(self):
        return f'{self.email} - {self.opinion}'
# Create your models here.

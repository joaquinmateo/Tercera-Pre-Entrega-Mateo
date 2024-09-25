from django.db import models

class Catalogo(models.Model):
    marca = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    precio = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.marca} - {self.producto} - ${self.precio}'
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f'{self.nombre} - {self.apellido}'
    class Meta():
        verbose_name = 'Client'
        verbose_name_plural = 'My Clients...'
        ordering = ('nombre', 'apellido')
    
class Opiniones(models.Model):
    opinion = models.CharField(max_length=250)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.cliente} - {self.opinion}'
# Create your models here.

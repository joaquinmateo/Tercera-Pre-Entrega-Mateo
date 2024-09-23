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
    
class Entrega(models.Model):
    direccion = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nombre}'
# Create your models here.

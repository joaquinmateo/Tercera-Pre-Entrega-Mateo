from django.contrib import admin
from .models import Catalogo, Cliente, Entrega

# Register your models here.
admin.site.register(Catalogo)
admin.site.register(Cliente)
admin.site.register(Entrega)


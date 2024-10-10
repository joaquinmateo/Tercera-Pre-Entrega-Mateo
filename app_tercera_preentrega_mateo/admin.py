from django.contrib import admin
from .models import Catalogo, Opiniones
from datetime import datetime

# Register your models here.

class CatalogoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'producto', 'precio', "imagen", "mostrar_imagen"]
    search_fields = ['marca', 'producto']
    list_filter = ['marca']

class OpinionesAdmin(admin.ModelAdmin):
    list_display = ['opinion']

admin.site.register(Catalogo, CatalogoAdmin)
admin.site.register(Opiniones, OpinionesAdmin)


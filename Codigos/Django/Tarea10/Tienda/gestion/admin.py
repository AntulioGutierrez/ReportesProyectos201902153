from django.contrib import admin

# Register your models here.
from .models import *

class clientesadmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "email", "telefono")
    search_fields=("nombre", "direccion", "email", "telefono")

class articulosadmin(admin.ModelAdmin):
    #list_filter= ("seccion")
    list_display=("nombre", "seccion", "precio")
    search_fields=("nombre", "seccion", "precio")
    
class pedidosadmin(admin.ModelAdmin):
    #list_filter= ("fecha", "entregado")
    list_display=("nombre", "fecha", "entregado")
    date_hierarchy=("fecha")
    
admin.site.register(clientes, clientesadmin)
admin.site.register(articulos, articulosadmin)
admin.site.register(pedidos, pedidosadmin)
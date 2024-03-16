from django.contrib import admin

# Register your models here.
from .models import *

class clientesadmin(admin.ModelAdmin):
    list_display=("usuario", "nombre", "direccion", "email", "telefono")
    #search_fields=("usuario", "nombre", "direccion", "email", "telefono")

class articulosadmin(admin.ModelAdmin):
    #list_filter= ("seccion")
    list_display=("nombre", "seccion", "precio")
    #search_fields=("nombre", "seccion", "precio")
    
class pedidosadmin(admin.ModelAdmin):
    #list_filter= ("fecha", "entregado")
    list_display=("cliente", "nombre", "fecha", "entregado")
    #date_hierarchy=("fecha")
    
class elementosadmin(admin.ModelAdmin):
    list_display=("producto", "pedido", "cantidad", "fecha")
    
class entregasadmin(admin.ModelAdmin):
    list_display=("cliente", "pedido", "direccion", "departamento", "municipio", "zona", "fecha")

admin.site.register(clientes, clientesadmin)
admin.site.register(articulos, articulosadmin)
admin.site.register(pedidos, pedidosadmin)
admin.site.register(elementos_pedido, elementosadmin)
admin.site.register(entregas, entregasadmin)
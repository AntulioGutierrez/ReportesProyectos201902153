from django.contrib import admin

# Register your models here.
from .models import *

class clientesadmin(admin.ModelAdmin):
    list_display=("usuario", "nombre", "direccion", "email", "telefono")
    #search_fields=("usuario", "nombre", "direccion", "email", "telefono")

class articulosadmin(admin.ModelAdmin):
    #list_filter= ("seccion")
    list_display=("nombre", "id", "seccion", "precio")
    #search_fields=("nombre", "seccion", "precio")
    
class pedidosadmin(admin.ModelAdmin):
    #list_filter= ("fecha", "entregado")
    list_display=("cliente", "id", "fecha", "entregado")
    #date_hierarchy=("fecha")
    
class elementosadmin(admin.ModelAdmin):
    list_display=("producto", "pedido", "cantidad", "fecha")
    
class entregasadmin(admin.ModelAdmin):
    list_display=("cliente", "pedido", "direccion", "departamento", "municipio", "zona", "fecha")

admin.site.register(Clientes, clientesadmin)
admin.site.register(Articulos, articulosadmin)
admin.site.register(Pedidos, pedidosadmin)
admin.site.register(Elementos_pedido, elementosadmin)
admin.site.register(Entregas, entregasadmin)
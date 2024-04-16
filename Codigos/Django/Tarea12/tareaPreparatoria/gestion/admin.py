from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import *

class contactosAdmin(admin.ModelAdmin):
    list_display=( "nombre", "id", "direccion", "email", "telefono")
    #search_fields=("usuario", "nombre", "direccion", "email", "telefono")

class historialAdmin(admin.ModelAdmin):
    #list_filter= ("seccion")
   list_display=("usuario", "id", "accion", "fecha")
    #search_fields=("nombre", "seccion", "precio")
    


admin.site.register(Contactos, contactosAdmin)
admin.site.register(Historial, historialAdmin)

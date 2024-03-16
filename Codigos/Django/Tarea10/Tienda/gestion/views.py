from django.shortcuts import render
from django.template import *
from .models import *
import json

# Create your views here.
def inicio(Request):
    context = {}
    return render(Request, 'apartados/inicio.html')

def mujeres(Request):
    consulta = articulos.objects.filter(seccion='mujer')
    context = {'productos': consulta}
    return render(Request, 'apartados/mujeres.html', context)
    
    
def nino(Request):
    consulta = articulos.objects.filter(seccion='niño')
    context = {'productos': consulta}
    return render(Request, 'apartados/ninos.html', context)



def hombres(request):
    consulta = articulos.objects.filter(seccion='hombre')
    context = {'productos': consulta}
    return render(request, 'apartados/hombres.html', context)


def carrito(Request):
    context = {}
    return render(Request, 'apartados/carrito.html')
def pago(Request):
    context = {}
    return render(Request, 'apartados/pago.html')
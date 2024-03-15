from django.shortcuts import render
from django.template import *

# Create your views here.
def inicio(Request):
    context = {}
    return render(Request, 'apartados/inicio.html')
def mujeres(Request):
    context = {}
    return render(Request, 'apartados/mujeres.html')
def nino(Request):
    context = {}
    return render(Request, 'apartados/ninos.html')
def hombres(Request):
    context = {}
    return render(Request, 'apartados/hombres.html')
def carrito(Request):
    context = {}
    return render(Request, 'apartados/carrito.html')
def pago(Request):
    context = {}
    return render(Request, 'apartados/pago.html')
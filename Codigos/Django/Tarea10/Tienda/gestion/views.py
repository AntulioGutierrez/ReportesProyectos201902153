from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utils import *

# Create your views here.
def inicio(request):

    datos = datosCarrito(request)
    numcarrito= datos['numcarrito']

    context = {'numcarrito':numcarrito}
    return render(request, 'apartados/inicio.html', context)


def mujeres(request):
    
    datos = datosCarrito(request)
    numcarrito= datos['numcarrito']

    consulta = Articulos.objects.filter(seccion='mujer')
    context = {'productos': consulta, 'numcarrito':numcarrito }
    return render(request, 'apartados/mujeres.html', context)    
    
def nino(request):
    datos = datosCarrito(request)
    numcarrito= datos['numcarrito']
        
    consulta = Articulos.objects.filter(seccion='niño')
    context = {'productos': consulta, 'numcarrito': numcarrito}
    return render(request, 'apartados/ninos.html', context)

def hombres(request):
    datos = datosCarrito(request)
    numcarrito= datos['numcarrito']
       
    consulta = Articulos.objects.filter(seccion='hombre')
    context = {'productos': consulta, 'numcarrito': numcarrito}
    return render(request, 'apartados/hombres.html', context)


def carrito(request):
    datos = datosCarrito(request)
    items= datos['agregados']
    pedido= datos['total']
    numcarrito= datos['numcarrito']

    context = {'agregados': items, 'total':pedido, 'numcarrito': numcarrito}
    return render(request, 'apartados/carrito.html', context)

def pago(request):
    datos = datosCarrito(request)
    items= datos['agregados']
    pedido= datos['total']
    numcarrito= datos['numcarrito']

    context = {'agregados': items, 'total':pedido, 'numcarrito': numcarrito}
    return render(request, 'apartados/pago.html', context)

def actualizarItem(request):
    data= json.loads(request.body)
    productoId = data['iddelarticulo']
    accion = data ['hacer']
    
    cliente = request.user.clientes
    producto = Articulos.objects.get(id = productoId)
    pedido, created = Pedidos.objects.get_or_create(cliente = cliente, entregado=False)
    pedidoElemento, created = Elementos_pedido.objects.get_or_create(pedido = pedido, producto = producto)
    
    if accion == 'agregar':
        pedidoElemento.cantidad = (pedidoElemento.cantidad +1)
        mensaje = 'cantidad sumada'

    elif accion == 'quitar':
        pedidoElemento.cantidad = (pedidoElemento.cantidad -1)
        mensaje = 'cantidad restada'
        
    pedidoElemento.save()
    
    if pedidoElemento.cantidad<= 0:
        pedidoElemento.delete()
        mensaje = 'elemento eliminado'
        
    return JsonResponse({'mensaje': mensaje}, safe=False)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def procesarOrden(request):
    transaccionid = datetime.datetime.now().timestamp()
    datosrecibidos = json.loads(request.body)

    if request.user.is_authenticated:
        mensaje = 'este es con usuario'
        cliente = request.user.clientes 
        pedido, created = Pedidos.objects.get_or_create(cliente=cliente, entregado=False)        
    else:
        mensaje = 'Usuario no ingresado o autentificado'
        cliente, pedido = ordenUsuarioNoingresado(request, datosrecibidos)
        
    total = datosrecibidos['Formulario']['total'].replace(',', '.')
    total = float(total)
    pedido.mas_infomracion = transaccionid
        
    if total == pedido.precio_del_carrito:
        pedido.entregado = True
        pedido.save()
    if pedido.entregado == True:
        Entregas.objects.create(
                cliente = cliente,
                pedido = pedido,
                direccion =datosrecibidos['Ubicacion']['direccion'],
                departamento =datosrecibidos['Ubicacion']['departamento'],
                municipio =datosrecibidos['Ubicacion']['municipio'],
                zona =datosrecibidos['Ubicacion']['zona'],
            )
        
    mensaje = 'Orden procesada'
        
    return JsonResponse({'mensaje': mensaje}, safe=False)

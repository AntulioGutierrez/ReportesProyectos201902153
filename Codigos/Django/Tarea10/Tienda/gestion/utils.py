import json
from .models import *

def cookieCarrito(request):
    items = []
    pedido = {'cantidad_del_carrito': 0, 'precio_del_carrito': 0}
    numcarrito = 0

    try:
        carrito = json.loads(request.COOKIES.get('carrito', '{}'))
    except json.JSONDecodeError:
        carrito = {}

    # Obtener todos los productos en una sola consulta
    productos_ids = carrito.keys()
    productos = Articulos.objects.filter(id__in=productos_ids)

    for producto in productos:
        cantidad = carrito[str(producto.id)]['quantity']
        total = producto.precio * cantidad

        numcarrito += cantidad
        pedido['precio_del_carrito'] += total
        pedido['cantidad_del_carrito'] += cantidad

        item = {
            'producto': {
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'imagenURL': producto.imagenURL,
            },
            'cantidad': cantidad,
            'total': total
        }
        items.append(item)

    return {'agregados': items, 'total': pedido, 'numcarrito': numcarrito}

def datosCarrito(request):
    if request.user.is_authenticated:
        cliente = request.user.clientes 
        #esto verifica si hay multiples pedidos del mismo usuario y elije el primero que encuentre empieza desde el 0 en adelante
        #pedidos = Pedidos.objects.filter(cliente=cliente, entregado=False)
        #if pedidos.exists():
        #    pedido = pedidos[0]  # Tomar el primer pedido si hay más de uno
        #    print('mensaje ', pedido)
        #else:
        #    pedido = Pedidos.objects.create(cliente=cliente, entregado=False)
        pedido, created = Pedidos.objects.get_or_create(cliente=cliente, entregado=False)
        items = pedido.elementos_pedido_set.all()  
        numcarrito = pedido.cantidad_del_carrito
    else:
        datosDelCookie = cookieCarrito(request)
        items= datosDelCookie['agregados']
        pedido= datosDelCookie['total']
        numcarrito= datosDelCookie['numcarrito']

    return {'agregados': items, 'total':pedido, 'numcarrito': numcarrito}

def ordenUsuarioNoingresado(request, datosrecibidos):
    
    print('cookie: ', request.COOKIES)
        
    nombre =datosrecibidos['Formulario']['nombre']
    direccion =datosrecibidos['Formulario']['direccion']
    email =datosrecibidos['Formulario']['email']
    telefono =datosrecibidos['Formulario']['telefono']
        
    datosDelCookie =datosCarrito(request)
    items = datosDelCookie['agregados']
    cliente, created = Clientes.objects.get_or_create(
            email = email,
            telefono = telefono,
        )
    cliente.nombre = nombre
    cliente.direccion = direccion
    cliente.save()
        
    pedido = Pedidos.objects.create(
            cliente =cliente,
            entregado = False,
        )
        
    for item in items:
        producto = Articulos.objects.get(id=item['producto']['id'])
            
        elementoPedido = Elementos_pedido.objects.create(
                producto = producto,
                pedido = pedido,
                cantidad =item['cantidad']
            )

    return cliente, pedido
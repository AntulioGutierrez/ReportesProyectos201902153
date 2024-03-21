from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Clientes (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre=models.CharField(max_length=30, null=False)
    direccion=models.CharField(max_length=30, null=False)
    email=models.EmailField(null=True, blank=True)
    telefono=models.CharField(max_length=8)
    def __str__(self):       
        return self.nombre
    
class Articulos(models.Model):
    nombre=models.CharField(max_length=30, null=False)
    seccion=models.CharField(max_length=30, null=False)
    precio=models.FloatField(null=False)
    imagen=models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.nombre
    
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url

    
class Pedidos(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True, blank=True)  
    fecha=models.DateTimeField(auto_now_add=True) 
    entregado=models.BooleanField(default=False, null=True, blank=True)
    mas_infomracion = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def precio_del_carrito(self):
        elementos_pedido = self.elementos_pedido_set.all()
        total = sum([item.precio_total for item in elementos_pedido])
        return total
    @property
    def cantidad_del_carrito(self):
        elementos_pedido = self.elementos_pedido_set.all()
        total = sum([item.cantidad for item in elementos_pedido])
        return total

    @property
    def entregadoaun(self):
        return True
          
class Elementos_pedido(models.Model):
    producto = models.ForeignKey(Articulos, on_delete=models.SET_NULL, null=True, blank=True)
    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    @property
    def precio_total(self):
        total = self.producto.precio * self.cantidad
        return total
    
class Entregas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True, blank=True)
    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True)
    departamento = models.CharField(max_length=200, null=True)
    municipio = models.CharField(max_length=200, null=True)
    zona = models.CharField(max_length=200, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.direccion
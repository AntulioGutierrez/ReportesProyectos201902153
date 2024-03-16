from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class clientes (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre=models.CharField(max_length=30, null=False)
    direccion=models.CharField(max_length=30, null=False)
    email=models.EmailField(null=True, blank=True)
    telefono=models.CharField(max_length=8)
    def __str__(self):       
        return self.nombre
    
class articulos(models.Model):
    nombre=models.CharField(max_length=30, null=False)
    seccion=models.CharField(max_length=30, null=False)
    precio=models.FloatField(null=False)
    imagen=models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class pedidos(models.Model):
    cliente = models.ForeignKey(clientes, on_delete=models.SET_NULL, null=True, blank=True)
    nombre=models.CharField(max_length=30)
    fecha=models.DateTimeField(auto_now_add=True) 
    entregado=models.BooleanField(default=False, null=True, blank=True)
    mas_infomracion = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.id)
    
class elementos_pedido(models.Model):
    producto = models.ForeignKey(articulos, on_delete=models.SET_NULL, null=True, blank=True)
    pedido = models.ForeignKey(pedidos, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
class entregas(models.Model):
    cliente = models.ForeignKey(clientes, on_delete=models.SET_NULL, null=True, blank=True)
    pedido = models.ForeignKey(pedidos, on_delete=models.SET_NULL, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True)
    departamento = models.CharField(max_length=200, null=True)
    municipio = models.CharField(max_length=200, null=True)
    zona = models.CharField(max_length=200, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.direccion
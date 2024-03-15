from django.db import models
# Create your models here.

class clientes (models.Model):
    nombre=models.CharField(max_length=30, null=False)
    direccion=models.CharField(max_length=30, null=False)
    email=models.EmailField(null=True, blank=True)
    telefono=models.CharField(max_length=8)

class articulos(models.Model):
    nombre=models.CharField(max_length=30, null=False)
    seccion=models.CharField(max_length=30, null=False)
    precio=models.FloatField(null=False)
    image = models.ImageField(null=True, blank=True)
    
class pedidos(models.Model):
    nombre=models.CharField(max_length=30)
    fecha=models.DateField() 
    entregado=models.BooleanField()
from django.db import models
from django.utils import timezone
# Create your models here.

class Contactos(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    direccion = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=8)
    def __str__(self):
        return self.direccion, self.nombre, self.telefono


class Historial(models.Model):
    usuario = models.CharField(max_length=30, null=False)
    accion = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.usuario, self.accion

    

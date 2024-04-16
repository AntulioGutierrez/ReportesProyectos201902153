from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *

from django.db.models import Q

# Create your views here.
@login_required
def Inicio(request):
    return render(request, 'inicio.html')

@login_required
def Programa(request):
    if request.method == 'POST':
        nuevo_contacto = Contactos(
            nombre=request.POST.get('nombre'),
            direccion=request.POST.get('direccion'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono')
        )
        nuevo_contacto.save()
        
        usuario_actual = request.user.username
        Historial.objects.create(usuario=usuario_actual, accion='Creación de contacto')
        return redirect('ver')
    else:
        return render(request, 'programa.html')

@login_required    
def ver(request):
    consulta = Contactos.objects.all()
    usuario_actual = request.user
    context = {'contactos': consulta, 'usuario': usuario_actual}
    
    
    #Historial.objects.create(usuario=usuario_actual, accion='Creación de contacto')
    
    return render(request, 'ver.html', context)

@login_required
def editar(request):
    datos = Contactos.objects.all()  
    context = {'contacto': datos}
    if request.method == 'POST':
        nombre_contacto = request.POST.get('nuevoNombre')  
        contacto = Contactos.objects.filter(nombre=nombre_contacto)

        if contacto.exists():
            contacto = contacto.first()
            contacto.nombre = request.POST.get('nuevoNombre')
            contacto.direccion = request.POST.get('nuevaDireccion')
            contacto.email = request.POST.get('nuevoEmail')
            contacto.telefono = request.POST.get('nuevoTelefono')

            contacto.save()  # Guardar los cambios en el registro existente

        usuario_actual = request.user.username
        Historial.objects.create(usuario=usuario_actual, accion='Modificación de contacto')
        return redirect('ver')   
        
    else:
        # Si no es una solicitud POST, simplemente renderiza el formulario
        return render(request, 'editar.html', context)

@login_required
def historialVista(request):
    queHace = Historial.objects.all()
    context = {'accion': queHace}
    return render(request, 'historial.html', context)

@login_required
def Borrar(request):
    if request.method == 'POST':
        cliente=request.POST.get('nombre')
        eliminar = Contactos.objects.get(nombre=cliente)
        eliminar.delete()
        
        usuario_actual = request.user.username
        Historial.objects.create(usuario=usuario_actual, accion='Eliminacion de contacto')
        return redirect('ver')
    else:
        return render(request, 'borrar.html')  

def Salir(request):
    logout(request)
    return redirect('/')

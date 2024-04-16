from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name="inicio"),
    path('programa/', views.Programa , name="programa"),
    path('ver/', views.ver , name="ver"),
    path('editar/', views.editar, name="editar"),
    path('historial/', views.historialVista, name="historial"),
    path('borrar/', views.Borrar, name="borrar"),
    path('salir/', views.Salir, name='salir'),
    

    # ... otras URLs
]

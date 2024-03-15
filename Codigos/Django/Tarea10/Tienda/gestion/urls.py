from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('mujer/', views.mujeres, name="mujeres"),
    path('niños/', views.nino, name="ninos"),
    path('hombres/', views.hombres, name="hombres"),
    path('carrito/', views.carrito, name="carrito"),
    path('pago/', views.pago, name="pago"),
]
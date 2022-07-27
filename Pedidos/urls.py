from django import views
from django.urls import path
from .import views

urlpatterns=[

  path('',views.procesar_pedido, name="procesar_pedido")


]
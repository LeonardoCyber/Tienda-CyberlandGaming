from urllib import request
from .carroPS5 import CarroPS5
from TiendaPS5.models import ProductoPS5
from django.shortcuts import redirect


def agregar_productoPS5(request, productoPS5_id):
    carroPS5=CarroPS5(request)
    productoPS5=ProductoPS5.objects.get(id=productoPS5_id)
    carroPS5.agregarPS5(productoPS5=productoPS5)
    return redirect("TiendaPS5")

def eliminar_productoPS5(request, productoPS5_id):
    carroPS5=CarroPS5(request)
    productoPS5=ProductoPS5.objects.get(id=productoPS5_id)
    carroPS5.eliminarPS5(productoPS5=productoPS5)
    return redirect("TiendaPS5")

def restar_productoPS5(request, productoPS5_id):
    carroPS5=CarroPS5(request)
    productoPS5=ProductoPS5.objects.get(id=productoPS5_id)
    carroPS5.restar_productoPS5(productoPS5=productoPS5)
    return redirect("TiendaPS5")

def limpiar_carroPS5(request, productoPS5_id):
    carroPS5=CarroPS5(request)
    carroPS5.limpiar_carroPS5()
    return redirect("TiendaPS5")



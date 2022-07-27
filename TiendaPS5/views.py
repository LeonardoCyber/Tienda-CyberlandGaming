from django.shortcuts import render
from .models import ProductoPS5

def tiendaps5(request):
    producto_ps5=ProductoPS5.objects.all()
    return render(request, "tiendaps5/tiendaPS5.html",{"productos_ps5":producto_ps5})

from django.shortcuts import render, HttpResponse
from CarroCompra.carro import Carro



def home(request):
    carro=Carro(request)
    return render(request, "CG_app/home.html")





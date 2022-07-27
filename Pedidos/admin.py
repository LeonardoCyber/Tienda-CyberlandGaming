from django.contrib import admin
from .models import Linea_pedidos, Pedidos


admin.site.register([Pedidos,Linea_pedidos])
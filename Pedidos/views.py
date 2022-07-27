from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Pedidos.models import Linea_pedidos,Pedidos
from Pedidos.models import Pedidos
from CarroCompra.carro import Carro
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


@login_required(login_url='/registro/logear')
def procesar_pedido(request):
    pedidos=Pedidos.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(Linea_pedidos(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedidos=pedidos
            ))
    
    Linea_pedidos.objects.bulk_create(lineas_pedido)
    enviar_mail(
        pedidos=pedidos,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email,

    )
    
    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedidos.html",{
        "pedidos":kwargs.get("pedidos"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombre_usuario":kwargs.get("nombre_usuario")
        })
    mensaje_texto=strip_tags(mensaje)
    from_email="sm26856368@gmail.com"
    to=kwargs.get("email_usuario")
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)



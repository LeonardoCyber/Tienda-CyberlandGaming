import django
from django.shortcuts import redirect, render
from .forms import Formulario_contacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    formulario_contacto=Formulario_contacto()
    if request.method=="POST":
        formulario_contacto=Formulario_contacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            apellido=request.POST.get("apellido")
            email=request.POST.get("email")
            direccion=request.POST.get("direccion")
            Comentario=request.POST.get("Comentario")
            
            email=EmailMessage("mensaje desde App django",
            "Nombre del usuario y apellido {} {} con Email {} y direccion {} escribe lo siguiente:\n\n {}".format(nombre,apellido,email,direccion,Comentario),
            "",["sm26856368@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?exito")
            except:
                return redirect("/contacto/?noValido")
    
    return render(request,"contacto/contacto.html", {"mi_formulario":formulario_contacto})
    
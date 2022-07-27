from django import forms

class Formulario_contacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    apellido=forms.CharField(label="Apellido" , required=True)
    email=forms.CharField(label="Email", required=True)
    direccion=forms.CharField(label="Dirección", required=True)
    Comentario=forms.CharField(label="Comentario", widget=forms.Textarea)
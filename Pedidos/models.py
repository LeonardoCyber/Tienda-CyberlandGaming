from django.db import models
from django.contrib.auth import get_user_model
from Tienda.models import Producto
from django.db.models import F , Sum, FloatField


User=get_user_model()


class Pedidos(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )['total']

    class Meta():
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']

class Linea_pedidos(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedidos=models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta():
        db_table='linea_pedidos'
        verbose_name='línea pedidos'
        verbose_name_plural='líneas pedidos'
        ordering=['id']

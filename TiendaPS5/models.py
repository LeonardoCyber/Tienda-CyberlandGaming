from django.db import models


class Categoria_productoPS5(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='categoria_productoPS5'
        verbose_name_plural='categorias_productoPS5'
    
    def __str__(self):
        return self.nombre

class ProductoPS5(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria_productoPS5, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='TiendaPS5', null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)


    class Meta:
        verbose_name='producto_ps5'
        verbose_name_plural='productos_ps5'


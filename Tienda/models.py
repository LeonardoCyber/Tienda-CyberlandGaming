from django.db import models

class Categoria_producto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='categoria_producto'
        verbose_name_plural='categorias_producto'
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria_producto, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='Tienda', null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)


    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'


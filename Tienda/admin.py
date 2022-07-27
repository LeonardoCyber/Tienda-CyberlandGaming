from django.contrib import admin
from .models import Categoria_producto, Producto

class Categoria_productoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class Producto_admin(admin.ModelAdmin):
    readonly_fields=("created","updated")


admin.site.register(Categoria_producto, Categoria_productoAdmin)
admin.site.register(Producto,Producto_admin)


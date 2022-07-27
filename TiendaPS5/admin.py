from django.contrib import admin
from .models import Categoria_productoPS5, ProductoPS5

class Categoria_productoPS5Admin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class ProductoPS5_admin(admin.ModelAdmin):
    readonly_fields=("created","updated")


admin.site.register(Categoria_productoPS5, Categoria_productoPS5Admin)
admin.site.register(ProductoPS5,ProductoPS5_admin)

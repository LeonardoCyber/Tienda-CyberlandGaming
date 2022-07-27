from django.urls import path
from .import views

app_name='carroPS5'

urlpatterns = [
  
    path("agregarPS5/<int:productoPS5_id>/", views.agregar_productoPS5, name="agregarPS5"),
    path("eliminarPS5/<int:productoPS5_id>/", views.eliminar_productoPS5, name="eliminarPS5"),
    path("restarPS5/<int:productoPS5_id>/", views.restar_productoPS5, name="restarPS5"),
    path("limpiarPS5/",views.limpiar_carroPS5, name="limpiarPS5"),

     


]

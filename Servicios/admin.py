from django.contrib import admin
from .models import Servicio


class Servicio_admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio, Servicio_admin)

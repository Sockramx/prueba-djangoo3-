from django.contrib import admin

# Register your models here.

from .models import Producto, Categoria, Proveedor, Empleado

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Empleado)

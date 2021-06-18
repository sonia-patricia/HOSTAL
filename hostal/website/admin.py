from django.contrib import admin
from .models import Empleado, Proveedor,Rubro_proveedor, Cliente, Producto, Usuarios, Ordenesdecompra, Orden_pedido

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Rubro_proveedor)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Usuarios)
admin.site.register(Empleado)
admin.site.register(Ordenesdecompra)
admin.site.register(Orden_pedido)


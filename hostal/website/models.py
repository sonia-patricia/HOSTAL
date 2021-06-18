import datetime
from django.db import models
from django.db.models.enums import Choices
from django.utils import timezone
from django.db.models.fields import EmailField, IntegerField, BigAutoField, DateField, DateTimeField, DateTimeCheckMixin
from django.urls import reverse
import uuid

# Create your models here.

class Rubro_proveedor(models.Model):
    id_rubro = models.BigAutoField(primary_key=True)
    rubro = models.CharField(max_length=25,null=False)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.rubro

class Proveedor(models.Model):
    rut_proveedor = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1, null=False)
    nombre = models.CharField(max_length=50,null=False)
    telefono = models.IntegerField(null=False)
    email = models.EmailField(null=False)
    direccion = models.CharField(max_length=100,null=False)
    id_rubro = models.ForeignKey(Rubro_proveedor,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('proveedores')
    
    def __str__(self):
        return self.nombre

class Orden_pedido(models.Model):
    numero_orden_p=models.BigAutoField(primary_key=True)
    fecha=models.DateField(null=False)
    neto=models.IntegerField(null=False)
    iva=models.IntegerField(null=False)
    total=models.IntegerField(null=False)
    rut_proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    #rut_empleado=models.IntegerField(primary_key=True)

    def get_absolute_url(self):
        return reverse('orden_pedido')

    def __str__(self):
        return '%s' % (self.numero_orden_p)

class Cliente(models.Model):

    rut_cliente = models.IntegerField(primary_key=True, help_text='')
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=25)
    telefono = models.IntegerField()
    email = models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)
    usuario = models.CharField(max_length=25)
    contrasenia = models.CharField(max_length=8)

    def get_absolute_url(self):
        return reverse('cliente-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombre


#Opciones de habitaciones
habitacion_estado = [
    ('Disponible', 'Disponible'),
    ('Asignada', 'Asignada'),
    ('En Mantención', 'En Mantención')
]  

habitacion_tipo_cama = [
    ('Individual', 'Individual'),
    ('Queen', 'Queen'),
    ('King', 'King')
]

habitacion_tipo= [
    ('Individual', 'Individual'),
    ('Doble', 'Doble')
]

class Habitacion(models.Model):

    numero_habitacion = models.IntegerField(primary_key=True, help_text='')
    tipo = models.CharField(max_length=25,
    null=False, blank=False,
    choices=habitacion_tipo,
    #default=1
    )    
    estado = models.CharField(max_length=25,null=False, blank=False, choices=habitacion_estado,
    #default=1
    )
    tipo_cama = models.CharField(max_length=25,
    null=False, blank=False,
    choices=habitacion_tipo_cama,
    #default=1
    )
    accesorios = models.CharField(max_length=50)
    precio = models.IntegerField()

    def get_absolute_url(self):
        return reverse('habitacion-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.numero_habitacion)
#fin de Opciones de habitaciones


# modelo base de datos producto
class Producto(models.Model):

    codigo_producto = models.IntegerField(primary_key=True, help_text='')
    nombre = models.CharField(max_length=25)
    familia=models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    fecha_elaboracion =models.DateField(default=timezone.now)
    fecha_vencimineto =models.DateField(default=timezone.now)
    stock= models.IntegerField()
    stock_critico=models.IntegerField()
    precio_unitario=models.IntegerField()
    item= models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('producto-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombre

tipo_perfil= [
    ('cambiar', 'cambiar'),
    ('agregar', 'agregar')
]
class Usuarios(models.Model):
    rut_usuarios=models.IntegerField(primary_key=True, help_text='' )
    dv=models.CharField(max_length=2)
    nombre_usuario=models.CharField(max_length=80, null=False)
    perfil = models.CharField(max_length=25, null=False, blank=False, choices=tipo_perfil)
    telefono=models.CharField(max_length=12,)
    email=models.EmailField(max_length=300)
    direccion=models.CharField(max_length=250,null=False)
    inicio_actividades=models.DateField(default=timezone.now)
    activo=models.BooleanField(default=True, verbose_name="Eres un usuario activo?")

    def get_absolute_url(self):
        return reverse('usuario-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombre_usuario
   

# JUAN
class Empleado(models.Model):

    rut_empleado = models.IntegerField(primary_key=True, help_text='')
    dv = models.CharField(max_length=1)
    nombres = models.CharField(max_length=25)
    a_paterno = models.CharField(max_length=25)
    a_materno = models.CharField(max_length=25)
    telefono = models.IntegerField()
    email = models.CharField(max_length=25)
    direccion = models.CharField(max_length=50)
    usuario = models.CharField(max_length=25)
    contrasenia = models.CharField(max_length=8)

    def get_absolute_url(self):
        return reverse('empleado-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombres


#juan
class Ordenesdecompra(models.Model):

    numero_orden_c = models.IntegerField(primary_key=True, help_text='')
    fecha_llegada = models.DateField(default=timezone.now)
    fecha_salida = models.DateField(default=timezone.now)
    total_dias = models.IntegerField()
    total_huespedes = models.IntegerField()

    def get_absolute_url(self):
        return reverse('ordenesdecompra-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.numero_orden_c)


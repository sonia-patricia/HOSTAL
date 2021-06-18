from django.db import models
from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Orden_pedido, Proveedor, Producto, Habitacion, Usuarios, Empleado, Ordenesdecompra
from django.views import generic
from django.db.models import Q


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'website/home.html')


def clientes(request):
    busqueda = request.GET.get("buscar")
    cliente = Cliente.objects.all()

    if busqueda:
        cliente = Cliente.objects.filter(
            Q(rut_cliente__icontains = busqueda) |
            Q(nombre__icontains = busqueda)
        ).distinct()

    return render(request, 'website/clientes.html', {'cliente':cliente}) 

def habitaciones(request):
    busqueda = request.GET.get("buscar")
    habitacion = Habitacion.objects.all()

    if busqueda:
        habitacion = Habitacion.objects.filter(
            Q(numero_habitacion__icontains = busqueda)
        ).distinct()

    return render(request, 'website/habitaciones.html', {'habitacion':habitacion})  
      
# vista producto
def producto(request):
    return render(request, 'website/producto.html')

# vista USUARIOS
def usuario(request):
    return render(request, 'website/usuario.html')

#EMPLEADOS JUAN

def empleados(request):
    busqueda = request.GET.get("buscar")
    empleado = Empleado.objects.all()

    if busqueda:
        empleado = Empleado.objects.filter(
            Q(rut_empleado__icontains = busqueda) |
            Q(nombres__icontains = busqueda)
        ).distinct()

    return render(request, 'website/empleados.html', {'empleado':empleado})

class EmpleadoCreate(CreateView):
    model = Empleado
    fields = '__all__'
    template_name = 'website/empleado_form.html'
    success_url = reverse_lazy('empleados_list')

class EmpleadoUpdate(UpdateView):
    model = Empleado
    fields = '__all__'
    success_url = reverse_lazy('empleados_list')

class EmpleadoDelete(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados_list')

class EmpleadoDetailView(generic.DetailView):
    model = Empleado    

class EmpleadoListView(generic.ListView):
    model = Empleado
    template_name = 'website/empleados_list.html'
     
#juan

def ordenesdecompra(request):
    busqueda = request.GET.get("buscar")
    ordenesdecompra = Ordenesdecompra.objects.all()

    if busqueda:
        ordenesdecompra = Ordenesdecompra.objects.filter(
            Q(numero_orden_c__icontains = busqueda)
        ).distinct()

    return render(request, 'website/ordenesdecompras.html', {'ordenesdecompra':ordenesdecompra})

class OrdenesdecompraCreate(CreateView):
    model = Ordenesdecompra
    fields = '__all__'
    template_name = 'website/ordenesdecompra_form.html'
    success_url = reverse_lazy('ordenesdecompras_list')

class OrdenesdecompraUpdate(UpdateView):
    model = Ordenesdecompra
    #fields = ['nombres','a.paterno','a.materno','telefono','email','direccion','usuario','contrasenia']    
    fields = '__all__'
    success_url = reverse_lazy('ordenesdecompras_list')

class OrdenesdecompraDelete(DeleteView):
    model = Ordenesdecompra
    success_url = reverse_lazy('ordenesdecompras_list')

class OrdenesdecompraDetailView(generic.DetailView):
    model = Ordenesdecompra    

class OrdenesdecompraListView(generic.ListView):
    model = Ordenesdecompra
    template_name = 'website/ordenesdecompras_list.html'



#sonia
class Orden_pedidoCreate(CreateView):
    model = Orden_pedido
    fields = '__all__'

class Orden_pedidoDetailView(generic.DetailView):
    model = Orden_pedido

class Orden_pedidoDelete(DeleteView):
    model = Orden_pedido
    success_url = reverse_lazy('orden_pedido')

class Orden_pedidoUpdate(UpdateView):
    model = Orden_pedido
    fields = '__all__'

class Orden_pedidoListView(generic.ListView):
    model = Orden_pedido
    template_name = 'website/orden_pedido_list.html'




class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'website/cliente_form.html'
    success_url = reverse_lazy('clientes_list')

class ClienteUpdate(UpdateView):
    model = Cliente
    #fields = ['nombre','telefono','email','direccion','usuario','contrasenia']    
    fields = '__all__'
    success_url = reverse_lazy('clientes_list')

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes_list')

class ClienteDetailView(generic.DetailView):
    model = Cliente    

class ClienteListView(generic.ListView):
    model = Cliente
    template_name = 'website/clientes_list.html'
    ordering = 'rut_cliente' 


class HabitacionCreate(CreateView):
    model = Habitacion
    fields = '__all__'
    template_name = 'website/habitacion_form.html'
    success_url = reverse_lazy('habitaciones_list')

class HabitacionListView(generic.ListView):
    model = Habitacion
    template_name = 'website/habitaciones_list.html'  
    ordering = 'numero_habitacion'  

class HabitacionUpdate(UpdateView):
    model = Habitacion
    fields = '__all__'
    success_url = reverse_lazy('habitaciones_list')  

class HabitacionDelete(DeleteView):
    model = Habitacion
    success_url = reverse_lazy('habitaciones_list')      
    



class ProveedorCreate(CreateView):
    model = Proveedor
    fields = '__all__'

class ProveedorDetailView(generic.DetailView):
    model = Proveedor

class ProveedorDelete(DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedores')

class ProveedorUpdate(UpdateView):
    model= Proveedor
    fields = '__all__'

class ProveedorListView(generic.ListView):
    model = Proveedor
    template_name = 'website/proveedor_list.html'





#Producto CRUD
class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'
    template_name = 'website/producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoUpdate(UpdateView):
    model = Producto
    #fields = ['nombre','telefono','email','direccion','usuario','contrasenia']    
    fields = '__all__'
    success_url = reverse_lazy('producto_list')

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto_list')

class ProductoDetailView(generic.DetailView):
    model = Producto    

class ProductoListView(generic.ListView):
    model = Producto
    template_name = 'website/producto_list.html'

#USUARIO CRUD
class UsuarioCreate(CreateView):
    model = Usuarios
    fields = '__all__'
    template_name = 'website/usuarios_form.html'
    success_url = reverse_lazy('usuario_list')

class UsuarioUpdate(UpdateView):
    model = Usuarios  
    fields = '__all__'
    success_url = reverse_lazy('usuario_list')

class UsuarioDelete(DeleteView):
    model = Usuarios
    success_url = reverse_lazy('usuario_list')

class UsuarioDetailView(generic.DetailView):
    model = Usuarios    

class UsuarioListView(generic.ListView):
    model = Usuarios
    template_name = 'website/usuario_list.html'





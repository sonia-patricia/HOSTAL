from django.shortcuts import render
from django.http.response import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente

from django.views import generic


# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def clientes(request):
    return render(request, 'website/clientes.html')   
     

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

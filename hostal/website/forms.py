from django import forms
from .models import Rubro_proveedor

class ProveedorForm(forms.Form):
    rut_proveedor=forms.IntegerField(label="Rut Proveedor",required=True)
    dv=forms.CharField(label="Digito verificador",required=True)
    nombre=forms.CharField(label="Nombre",required=True)
    telefono=forms.IntegerField(label="Telefono",required=True)
    email=forms.EmailField(label="Email",required=True)
    direccion=forms.CharField(label="direccion",required=True)
    id_rubro=forms.ModelChoiceField(queryset=Rubro_proveedor.objects.all())


from typing import Text
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.forms.widgets import TextInput
from .models import Cliente, Habitacion, Huesped, Reserva, ReservaHuesped

GRUPOS = [
    ('1', 'Administrador'),
    ('2', 'Empleado'),
    ('3', 'Cliente'),
    ('4','Proveedor')
]

class UsuarioCreateForm(UserCreationForm):

    grupo_usuario = forms.ChoiceField(
        choices=GRUPOS,
        required=True,
    )
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                 'class': 'form-control'
            }
        )        
    )

    grupo_usuario.widget.attrs.update({'class':'form-control'})

    def save(self, commit=True,grupo_usuario=None):
        user = super().save(commit=False)
        if commit:
            if super().save(commit=True):
                if grupo_usuario == 1:
                    group = Group.objects.get(name='Administrador')
                elif grupo_usuario == 2:
                    group = Group.objects.get(name='Empleado')
                elif grupo_usuario == 3:
                    group = Group.objects.get(name='Cliente')       
                elif grupo_usuario == 4:
                    group = Group.objects.get(name='Proveedor')

                user.groups.add(group)

        else:
            return user
        

class UsuarioUpdateForm(forms.ModelForm):

    username = forms.CharField(
        label='Usuario',
        required=False,
        widget=forms.TextInput(
            attrs={
                 'class': 'form-control'
            }
        )        
    )

    grupo_usuario = forms.ChoiceField(
        label='Grupo usuario',
        choices=GRUPOS,
        required=True,
    )    

    grupo_usuario.widget.attrs.update({'class':'form-control'})

    class Meta:
        model = User
        fields = ('username',)

    def save(self,commit=True,user=None,username=None,grupo_usuario_i=None):
        
        if commit:
            if username != user.username:
                User.objects.filter(id=user.id).update(username=username)

            if grupo_usuario_i != None:
                grupo_usuario = int(grupo_usuario_i)
                
                user.groups.clear()

                if grupo_usuario == 1:
                    group = Group.objects.get(name='Administrador')
                elif grupo_usuario == 2:
                    group = Group.objects.get(name='Empleado')
                elif grupo_usuario == 3:
                    group = Group.objects.get(name='Cliente')       
                elif grupo_usuario == 4:
                    group = Group.objects.get(name='Proveedor')

                user.groups.add(group)

class ReservaCreateForm(forms.ModelForm):

    cliente = forms.ModelChoiceField(
        label='Cliente',
        queryset=Cliente.objects.all(),
        required=True
    )

    fecha_desde = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Fecha Desde',
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
            }
        )
    )

    fecha_hasta = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Fecha Hasta',
        widget=forms.DateInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    cliente.widget.attrs.update({'class':'form-control'})
    
    class Meta:
        model = Reserva 
        fields = ['cliente','fecha_desde','fecha_hasta']

class ReservaUpdateForm(forms.ModelForm):

    id_reserva = forms.IntegerField(
        label = 'ID Reserva',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'readonly':True,
            }
        )
    )

    cliente = forms.ModelChoiceField(
        label='Cliente',
        queryset=Cliente.objects.all(),
        required=True
    )

    fecha_desde = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Fecha Desde',
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
            }
        )
    )

    fecha_hasta = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Fecha Hasta',
        widget=forms.DateInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    cliente.widget.attrs.update({'class':'form-control'})
    
    class Meta:
        model = Reserva 
        fields = ['id_reserva','cliente','fecha_desde','fecha_hasta']

class AddHuespedReservaForm(forms.ModelForm):

    class Meta:
        model = ReservaHuesped
        fields = ['rut_huesped','habitacion']

    rut_huesped = forms.ModelChoiceField(
        label = 'Huésped',
        queryset = Huesped.objects.all(),
        required  =True
    )

    habitacion = forms.ModelChoiceField(
        label = 'Habitación',
        queryset = Habitacion.objects.all(),
        required = True
    )

    rut_huesped.widget.attrs.update({'class':'form-control mb-2 mr-sm-2'})
    habitacion.widget.attrs.update({'class':'form-control mb-2 mr-sm-2'})
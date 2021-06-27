from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

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
        


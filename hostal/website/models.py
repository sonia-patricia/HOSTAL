from django.db import models
from django.urls import reverse
import uuid

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

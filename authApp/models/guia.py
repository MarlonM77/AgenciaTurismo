from django.db import models
from .tipo_turismo import TipoTurismo

class Guia(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_turismo = models.ForeignKey(TipoTurismo, related_name='guia', on_delete=models.CASCADE)
    nombre = models.CharField('Name', max_length = 30)
    datos = models.CharField('json_datos', max_length = 30)
    foto = models.CharField('foto', max_length = 30)
    contacto = models.CharField('telefono', max_length = 30)
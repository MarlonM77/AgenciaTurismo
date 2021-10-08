from django.db import models
from .tipo_turismo import TipoTurismo
from authApp.models import tipo_turismo

class Lugar(models.Model):
    id = models.AutoField(primary_key=True) 
    tipo_turismo = models.ForeignKey(TipoTurismo, related_name='lugar', on_delete=models.CASCADE)
    nombre = models.CharField('Name', max_length = 30)
    ubicacion = models.CharField('ubicacion', max_length = 30)
    json_fotos = models.CharField('json_fotos', max_length = 30)
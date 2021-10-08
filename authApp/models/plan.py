from django.db import models
from .tipo_turismo import TipoTurismo

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_turismo = models.ForeignKey(TipoTurismo, related_name='plan', on_delete=models.CASCADE)
    nombre = models.CharField('Name', max_length = 30)
    descripcion = models.CharField('descripcion', max_length = 30)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    valor = models.IntegerField(default=0)
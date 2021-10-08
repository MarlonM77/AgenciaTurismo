from django.db import models

class TipoTurismo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_tipo_turismo = models.CharField('tipo_turismo', max_length = 30)
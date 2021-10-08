from django.db import models

class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Name', max_length = 30)
    ubicacion = models.CharField('ubicacion', max_length = 30)
    json_fotos = models.CharField('json_fotos', max_length = 30)
    contacto = models.CharField('telefono', max_length = 30)
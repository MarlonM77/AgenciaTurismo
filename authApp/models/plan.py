from django.db                   import models
from authApp.models.user         import User


class Plan(models.Model):

    id              = models.AutoField(primary_key = True)
    user            = models.ForeignKey(User, related_name = "user", on_delete = models.CASCADE)
    valor           = models.IntegerField(null = True, blank = True)
    fecha_inicio    = models.DateTimeField(null = True, blank = True)
    fecha_fin       = models.DateTimeField(null = True, blank = True)
    nombre_plan     = models.CharField('Plan', max_length = 30, null = True, blank = True)
    descripcion     = models.CharField('Descripcion', max_length = 255, null = True, blank = True)
    cant_personas   = models.IntegerField(null = True, blank = True)



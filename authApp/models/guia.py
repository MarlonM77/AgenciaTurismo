from django.contrib.auth.base_user import AbstractBaseUser
from django.db                   import models
from django.contrib.auth.models  import AbstractUser, PermissionsMixin
from .user                       import User

class User_guia(AbstractBaseUser, PermissionsMixin):

    id      = models.AutoField(primary_key = True)
    user         = models.ForeignKey(User, related_name='guia', on_delete = models.CASCADE)
    foto         = models.ImageField(null = True, blank = True)
    nombre       = models.CharField('Name',        max_length = 30)
    cedula       = models.CharField('cedula',      max_length = 30)
    contacto     = models.CharField('telefono',    max_length = 30)
    tipo_turismo = models.CharField('Turismo',     max_length = 30)
    descripcion  = models.CharField('Descripcion', max_length = 255)
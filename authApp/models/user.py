from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager, update_last_login
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):

    def create_user(self, username, password = None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('El usuario requiere un nombre')
        user = self.model(username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username_, password_):
        """
        Creates and saves a superuser with the given username and password.
        """
        user         = self.create_user(
            username = username_,
            password = password_
        )
        user.is_admin = True
        user.save(using = self._db)
        return user
        
def user_directory_path(instance, filename):
    return 'Profiles/{0}/{1}'.format(instance.title, filename)

class User(AbstractBaseUser, PermissionsMixin):

    id       = models.BigAutoField(primary_key=True)
    foto     = models.ImageField(upload_to = user_directory_path, blank = True, null = True)
    username = models.CharField('Username',   max_length = 15, unique=True)
    password = models.CharField('Password',   max_length = 256)
    name     = models.CharField('Fullname',   max_length = 50)
    email    = models.EmailField('Email',     max_length = 100, unique=True)


    def save(self, **kwargs):
        some_salt     = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects         = UserManager()
    USERNAME_FIELD  = 'username'    



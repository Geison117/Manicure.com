from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, apellidos, telefono, password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        usuario = self.model(username = username,
                             email = self.normalize_email(email),
                             nombres = nombres,
                             apellidos = apellidos,
                             telefono = telefono
                             )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email, username, nombres, apellidos, telefono, password):
        usuario = self.create_user(
                             email,
                             username=username,
                             nombres=nombres,
                             apellidos=apellidos,
                             telefono=telefono,
                             password = password
                             )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario



class Cliente(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique = True, max_length=100)
    password = models.CharField('Contraseña', max_length = 100)
    email = models.EmailField('Correo Electrónico', unique = True, max_length=200)
    nombres = models.CharField('Nombres', max_length = 100, blank = True, null= True)
    apellidos = models.CharField('Apellidos', max_length = 100, blank = True, null= True)
    telefono = models.IntegerField('Telefono',  blank = True, null= True)
    usuario_activo = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default = False)
    objects = UsuarioManager()
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos', 'telefono']



    def __str__(self):
        return self.username

    def has_perm(self, perm, obj= None):
        return True

    def has_module_perms(self, app_labels):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador


class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100, verbose_name='Contraseña')
    correo = models.EmailField(max_length=200)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    duracion = models.FloatField()
    foto = models.ImageField(upload_to='images/', null=True, blank = True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    total_factura = models.IntegerField()


class Cita(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    fecha = models.DateTimeField()


class Servicio_Cita(models.Model):
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

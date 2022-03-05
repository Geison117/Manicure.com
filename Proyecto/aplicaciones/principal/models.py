from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100, verbose_name='Constraseña')
    correo = models.EmailField(max_length=200)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre


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

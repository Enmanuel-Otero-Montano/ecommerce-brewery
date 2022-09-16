from distutils.command.upload import upload
from django.db import models
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import CharField

# Create your models here.

class Distribuidor(models.Model):
    nombre = models.CharField(max_length = 40)
    direccion = models.CharField(max_length = 60)
    email = models.EmailField()
    telefono = PhoneNumberField()
    sitio_web = models.URLField(blank = True)

    class Meta:
        verbose_name_plural = "Distribuidores"

    def __str__(self):
        return self.nombre


class Cerveza(models.Model):
    foto = models.ImageField(upload_to="foto")
    marca = models.CharField(max_length = 25)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    descripción = models.TextField()
    stock = models.PositiveIntegerField()
    precio = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    tamaño = models.PositiveIntegerField()
    grado_alcohol = models.DecimalField(max_digits = 2, decimal_places = 1, default = 00)
    TIPO = (
        ("nacional", "Nacional"),
        ("importada", "Importada"),
    )
    tipo = models.CharField(max_length = 9, choices = TIPO, default = "nacional")
    VAR = (
        ("ipa", "Ipa"),
        ("lager", "Lager"),
        ("ale", "Ale")
    )
    variedad = models.CharField(max_length = 5, choices = VAR, default = "lager")
    ENVASE = (
        ("lata", "Lata"),
        ("botella", "Botella")
    )
    envase = models.CharField(max_length = 7, choices = ENVASE, default = "botella")

    def __str__(self):
        return self.marca


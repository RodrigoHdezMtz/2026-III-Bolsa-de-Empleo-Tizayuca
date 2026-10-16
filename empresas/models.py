from django.conf import settings
from django.db import models


class Empresa(models.Model):
    TIPOS = [
        ('industrial', 'Industrial'),
        ('local', 'Negocio local'),
    ]
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    giro = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    verificada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
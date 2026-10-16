from django.conf import settings
from django.db import models


class Habilidad(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name_plural = 'habilidades'

    def __str__(self):
        return self.nombre


class Candidato(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True)
    colonia = models.CharField(max_length=100, blank=True)
    escolaridad = models.CharField(max_length=100, blank=True)
    resumen = models.TextField(blank=True)
    cv = models.FileField(upload_to='cv/', blank=True)
    habilidades = models.ManyToManyField(Habilidad, blank=True)

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username


class Experiencia(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name='experiencias')
    puesto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.puesto} en {self.empresa}'
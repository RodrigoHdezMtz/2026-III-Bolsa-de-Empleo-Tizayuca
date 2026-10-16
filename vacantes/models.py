from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nombre


class Vacante(models.Model):
    empresa = models.ForeignKey('empresas.Empresa', on_delete=models.CASCADE, related_name='vacantes')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='vacantes')
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    requisitos = models.TextField(blank=True)
    sueldo_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sueldo_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    horario = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    destacada = models.BooleanField(default=False)
    activa = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.titulo} - {self.empresa}'

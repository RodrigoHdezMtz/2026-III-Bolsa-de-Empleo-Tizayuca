from django.db import models


class Postulacion(models.Model):
    ESTADOS = [
        ('enviada', 'Enviada'),
        ('vista', 'Vista'),
        ('entrevista', 'Entrevista'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    ]
    candidato = models.ForeignKey('candidatos.Candidato', on_delete=models.CASCADE, related_name='postulaciones')
    vacante = models.ForeignKey('vacantes.Vacante', on_delete=models.CASCADE, related_name='postulaciones')
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='enviada')
    mensaje = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'postulaciones'
        constraints = [
            models.UniqueConstraint(fields=['candidato', 'vacante'], name='postulacion_unica'),
        ]

    def __str__(self):
        return f'{self.candidato} -> {self.vacante}'

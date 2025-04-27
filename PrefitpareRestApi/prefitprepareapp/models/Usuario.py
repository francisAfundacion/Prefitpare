from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('asesor', 'Asesor'),
        ('estandar','Estandar')
    )
    telefono = models.CharField(max_length=9),
    nombre = models.CharField(max_length=50),
    rol = models.CharField(choices=ROLES, default='estandar'),
    #A futuro tendremos una imagen de perfil por defecto.
    ImagenPerfil = models.URLField(null=True, blank=True)

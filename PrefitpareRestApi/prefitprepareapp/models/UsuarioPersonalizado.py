from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioPersonalizado(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('asesor', 'Asesor'),
        ('estandar','Estandar')
    ]
    telefono = models.CharField( max_length=9),
    nombre = models.CharField( max_length=50),
    rol = models.CharField( choices=ROLES, default='estandar'),
    #A futuro tendremos una imagen de perfil por defecto.
    Imagen_perfil = models.URLField( null=True, blank=True)

    # Añadir related_name para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',  # Cambiar el nombre de la relación inversa
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions_set',  # Cambiar el nombre de la relación inversa
        blank=True
    )

from django.db import models
from abc import abstractmethod

class ModeloBase(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_insercion = models.DateField( auto_now_add=True)

    class Meta:
        abstract = True

    @abstractmethod
    def __str__(self):
        pass


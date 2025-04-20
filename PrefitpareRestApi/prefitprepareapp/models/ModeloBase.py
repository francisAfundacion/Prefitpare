from django.db import models
from abc import abstractmethod

class ModeloBase(models.Model):
    nombre = models.CharField(40, unique=True),
    descripcion = models.TextField(blank=True, null=True),
    fechaInsercion = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

    @abstractmethod
    def __str__(self):
        pass


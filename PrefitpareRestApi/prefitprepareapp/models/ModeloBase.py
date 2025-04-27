from django.db import models
from abc import abstractmethod

class ModeloBase(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(blank=True)
    fechaInsercion = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

    @abstractmethod
    def __str__(self):
        pass


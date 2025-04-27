from ..enums.NombreClaseMapeado import generarMensajeMapeoObjeto
from ..models.ModeloBase import ModeloBase
from ..models.Categoria import Categoria
from ..models.PersonaTipo import PersonaTipo
from django.db import models

class Plato(ModeloBase):
    categoria = models.ManyToManyField(Categoria)
    personaTipo = models.ManyToManyField(PersonaTipo)
    peso = models.DecimalField(max_digits=3, decimal_places=2) #Campo decimal 2.23 => kg
    origenPais = models.CharField(max_length=40)

    def __str__(self):
        return generarMensajeMapeoObjeto(4) + " " + self.nombre
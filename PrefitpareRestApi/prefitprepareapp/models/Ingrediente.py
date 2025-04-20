from ..enums.NombreClaseMapeado import generarMensajeMapeoObjeto
from ..models.ModeloBase import ModeloBase
from ..models.Categoria import Categoria
from django.db import models

class Ingrediente(ModeloBase):
    categoria = models.ManyToManyField(Categoria, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=3, decimal_places=2)
    kcalPorGramo = models.DecimalField(max_digits=5, decimal_places=2)
    origenPais = models.CharField(40)

    def __str__(self):
        return generarMensajeMapeoObjeto(self, 3)
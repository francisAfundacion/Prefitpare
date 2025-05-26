from ..enums.NombreClaseMapeado import generar_mensaje_mapeo_objeto
from ..models.ModeloBase import ModeloBase
from ..models.Categoria import Categoria
from ..models.Ingrediente import Ingrediente
from ..models.TipoPersona import TipoPersona
from django.db import models

class Plato(ModeloBase):
    categorias = models.ManyToManyField(Categoria)
    tipos_persona = models.ManyToManyField(TipoPersona)
    ingredientes = models.ManyToManyField(Ingrediente)
    peso = models.DecimalField(max_digits=3, decimal_places=2) #Campo decimal 2.23 => kg
    origen_pais = models.CharField(max_length=40)

    def __str__(self):
        return generar_mensaje_mapeo_objeto(4) + " " + self.nombre
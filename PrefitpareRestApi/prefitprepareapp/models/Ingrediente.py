from ..enums.NombreClaseMapeado import generar_mensaje_mapeo_objeto
from ..models.ModeloBase import ModeloBase
from ..models.Categoria import Categoria
from django.db import models

class Ingrediente(ModeloBase):
    categorias = models.ManyToManyField(Categoria)
    peso = models.DecimalField(max_digits=3, decimal_places=2)
    kcal_por_gramo = models.DecimalField(max_digits=5, decimal_places=2)
    origen_pais = models.CharField(max_length=40)

    def __str__(self):
        return generar_mensaje_mapeo_objeto(3) + " " + self.nombre
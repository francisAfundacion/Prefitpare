
from ..enums.NombreClaseMapeado import generar_mensaje_mapeo_objeto
from ..models.ModeloBase import ModeloBase

class Categoria(ModeloBase):
    def __str__(self):
        return generar_mensaje_mapeo_objeto(1)  + " " + self.nombre
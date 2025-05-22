from ..enums.NombreClaseMapeado import generar_mensaje_mapeo_objeto
from ..models.ModeloBase import ModeloBase

class TipoPersona(ModeloBase):
    def __str__(self):
        return generar_mensaje_mapeo_objeto(2) + " " + self.nombre
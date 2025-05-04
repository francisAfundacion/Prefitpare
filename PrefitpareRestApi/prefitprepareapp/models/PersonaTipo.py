from ..enums.NombreClaseMapeado import generarMensajeMapeoObjeto
from ..models.ModeloBase import ModeloBase

class PersonaTipo(ModeloBase):
    def __str__(self):
        return generarMensajeMapeoObjeto(2) + " " + self.nombre
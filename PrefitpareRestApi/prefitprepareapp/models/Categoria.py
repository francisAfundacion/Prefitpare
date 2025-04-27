from prefitprepareapp.enums.NombreClaseMapeado import generarMensajeMapeoObjeto
from ..models.ModeloBase import ModeloBase

class Categoria(ModeloBase):
    def __str__(self):
        return generarMensajeMapeoObjeto(1)  + " " + self.nombre
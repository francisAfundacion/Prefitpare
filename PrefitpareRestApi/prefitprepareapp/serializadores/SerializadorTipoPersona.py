from .SerializadorBase import SerializadorBase
from prefitprepareapp.models import TipoPersona

class SerializadorTipoPersona(SerializadorBase):

    class Meta:
        model = TipoPersona
        fields = ['id', 'nombre', 'descripcion', 'fecha_insercion']

    def crear(self, **kwargs):
        return super().crear(**kwargs)

    def modificar(self, id, **kwargs):
        return super().modificar(id, **kwargs)

    def eliminar(self, id):
        return super().eliminar(id)
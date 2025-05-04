from .SerializadorBase import SerializadorBase
from prefitprepareapp.models import Categoria

class SerializadorCategoria(SerializadorBase):

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'fechaInsercion']

    def crear(self, **kwargs):
        return super().crear(**kwargs)

    def modificar(self, id, **kwargs):
        return super().modificar(id, **kwargs)

    def eliminar(self, id):
        return super().eliminar(id)





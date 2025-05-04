from .SerializadorBase import SerializadorBase
from .SerializadorCategoria import SerializadorCategoria
from prefitprepareapp.models import Ingrediente


class SerializadorIngrediente(SerializadorBase):

    categoria = SerializadorCategoria(many=True)

    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre','descripcion', 'fechaInsercion', 'categoria', 'peso', 'kcalPorGramo', 'origenPais']

    def crear(self, **kwargs):
        return super().crear(**kwargs)

    def modificar(self, id, **kwargs):
        return super().modificar(id, **kwargs)

    def eliminar(self, id):
        return super().eliminar(id)
from .SerializadorBase import SerializadorBase
from .SerializadorCategoria import SerializadorCategoria
from prefitprepareapp.models import Ingrediente


class SerializadorIngrediente(SerializadorBase):

    categorias = SerializadorCategoria(many=True)

    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre','descripcion', 'fecha_insercion', 'categorias', 'peso', 'kcal_por_gramo', 'origen_pais']

    def crear(self, **kwargs):
        return super().crear(**kwargs)

    def modificar(self, id, **kwargs):
        return super().modificar(id, **kwargs)

    def eliminar(self, id):
        return super().eliminar(id)
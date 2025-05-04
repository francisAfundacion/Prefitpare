from .SerializadorBase import SerializadorBase
from .SerializadorPersonaTipo import SerializadorPersonaTipo
from .SerializadorCategoria import SerializadorCategoria
from .SerializadorIngrediente import SerializadorIngrediente
from prefitprepareapp.models import Plato
from prefitprepareapp.models import Categoria
from prefitprepareapp.models import PersonaTipo

class SerializadorPlato(SerializadorBase):

    #Futuro control que el ingrediente no tenga mayor peso que el propio plato

    ingrediente = SerializadorIngrediente(many=True)
    categoria = SerializadorCategoria(many=True)
    personaTipo = SerializadorPersonaTipo(many=True)

    class Meta:
        model = Plato
        fields = ['id', 'nombre', 'descripcion', 'fechaInsercion', 'categoria', 'personaTipo', 'ingrediente', 'peso', 'origenPais']

        def crear(self, **kwargs):
            return super().crear(**kwargs)

        def modificar(self, id, **kwargs):
            return super().modificar(id, **kwargs)

        def eliminar(self, id):
            return super().eliminar(id)


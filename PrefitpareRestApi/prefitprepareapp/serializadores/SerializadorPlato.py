from .SerializadorBase import SerializadorBase
from .SerializadorTipoPersona import SerializadorTipoPersona
from .SerializadorCategoria import SerializadorCategoria
from .SerializadorIngrediente import SerializadorIngrediente
from prefitprepareapp.models import Plato

class SerializadorPlato(SerializadorBase):

    #Futuro control que el ingrediente no tenga mayor peso que el propio plato

    ingrediente = SerializadorIngrediente(many=True)
    categoria = SerializadorCategoria(many=True)
    tipo_persona = SerializadorTipoPersona(many=True)

    class Meta:
        model = Plato
        fields = ['id', 'nombre', 'descripcion', 'fecha_insercion', 'ingrediente', 'categoria', 'tipo_persona', 'peso', 'origen_pais']

    def crear(self, **kwargs):
        return super().crear(**kwargs)

    def modificar(self, id, **kwargs):
         return super().modificar(id, **kwargs)

    def eliminar(self, id):
        return super().eliminar(id)


from .SerializadorBase import SerializadorBase
from .SerializadorCategoria import SerializadorCategoria
from prefitprepareapp.models import Ingrediente


class SerializadorIngrediente(SerializadorBase):
    """
    Serializador que extiende SerializadorBase y proporciona la referencia al modelo Ingrediente,
    permitiendo ejecutar la estrategia concreta para cada método CRUD.

    Los métodos CRUD definidos funcionan como proxies que reciben los argumentos del cuerpo de la petición
    y/o el id (en caso de PUT, PATCH, DELETE), y los delegan al serializador padre.
    """

    categorias = SerializadorCategoria(many=True)

    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre','descripcion', 'fecha_insercion', 'categorias', 'peso', 'kcal_por_gramo', 'origen_pais']

    def crear(self, **kwargs):
        """
        Proxy que delega la creación al método crear del SerializadorBase

        Parámetros:
            **kwargs: Diccionario descomprimido con los campos para crear la instancia.

        Retorna:
            Instancia creada del modelo correspondiente.
        """
        return super().crear(**kwargs)

    def modificar(self, id, **kwargs):
        """
        Proxy que delega la creación al método crear del SerializadorBase

        Parámetros:
            **kwargs: Diccionario descomprimido con los campos para modificar la instancia.
            id (int): Identificador del objeto Ingrediente a modificar.

        Retorna:
            Instancia creada del modelo correspondiente.
        """
        return super().modificar(id, **kwargs)

    def eliminar(self, id):
        """
          Proxy que delega la eliminación al método eliminar del SerializadorBase.

          Parámetros:
              id (int): Identificador del objeto Ingrediente a eliminar.
          """
        return super().eliminar(id)
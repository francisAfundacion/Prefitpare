from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from prefitprepareapp.models import  ModeloBase
from prefitprepareapp.models import Categoria
from prefitprepareapp.models import TipoPersona
from prefitprepareapp.models import Ingrediente
from prefitprepareapp.servicios.ServicioSerializadorBase import ServicioSerializadorBase
from prefitprepareapp.infraestructura.GestorConsulta import GestorConsulta

class SerializadorBase(serializers.ModelSerializer):
    """
    Serializador base que proporciona una interfaz común para operaciones CRUD genéricas a través de un servicio.
    Por otra parte cumple los siguientes propósitos:

    1. Formateo bidireccional de datos.

    2. Delega al servicio el método http solicitado y la referencia del modelo asociado.
    """

    servicio = ServicioSerializadorBase()

    def crear(self, **kwargs):
        """
        Proxy que delega la creación del objeto a la capa de servicio

        Parámetros:
            **kwargs: Diccionario descomprimido con los campos para crear la instancia.
            Model: referencia modelo asociado a la petición http

        Retorna:
            Instancia creada del modelo correspondiente.
        """
        return self.servicio.crear(kwargs, self.Meta.model)

    def modificar(self, id, **kwargs):
        """
         Proxy que delega la modificación del objeto al método modificar de la capa de servicio.

         Parámetros:
             **kwargs: Diccionario descomprimido con los campos para modificar la instancia.
             id (int): Identificador del objeto  a modificar.
             Model: referencia modelo asociado a la petición http

         Retorna:
             Instancia  del modelo modificado correspondiente.
         """
        return self.servicio.modificar(id, kwargs, self.Meta.model)

    def eliminar(self, id):
        """
          Proxy que delega la elminación  del objeto al método eliminar de la  capa de servicio.

          Parámetros:
              id (int): Identificador del objeto a modificar.
              Model: referencia modelo asociado a la petición http.

          Retorna:
              Detalle del objeto eliminado.
          """
        return self.servicio.eliminar(id, self.Meta.model)







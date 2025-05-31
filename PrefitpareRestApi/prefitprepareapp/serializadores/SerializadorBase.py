from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from prefitprepareapp.models import  ModeloBase
from prefitprepareapp.models import Categoria
from prefitprepareapp.models import TipoPersona
from prefitprepareapp.models import Ingrediente
from prefitprepareapp.servicios.ServicioSerializadorBase import ServicioSerializadorBase
from prefitprepareapp.infraestructura.GestorConsulta import GestorConsulta

# Agregar comprobacion de existencia de los registros post, put, patch
# Comprobar si no encontrado
# TO-DO => SIMPLIFICAR Y HACERLO MÁS LEGIBLE EL CÓDIGO

class SerializadorBase(serializers.ModelSerializer):

    servicio = ServicioSerializadorBase()

    def crear(self, **kwargs):
        return self.servicio.crear(kwargs, self.Meta.model)

    def modificar(self, id, **kwargs):
        return self.servicio.modificar(id, kwargs, self.Meta.model)

    def eliminar(self, id):
        return self.servicio.eliminar(id, self.Meta.model)







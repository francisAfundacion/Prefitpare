from typing import Type
from django.db.models import Model

class GestorConsulta:

    def get_lista_objetos(self, lista_nombre_objetos_fk, modelo: Type[Model]):
        return modelo.objects.filter(nombre__in=lista_nombre_objetos_fk)

    def get_objeto_por_id(self, id, modelo: Type[Model]):
        return modelo.objects.get(id=id)



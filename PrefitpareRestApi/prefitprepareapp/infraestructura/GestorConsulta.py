from typing import Type
from django.db.models import Model

class GestorConsulta:

    def get_lista_objetos(self, modelo, lista_nombre_fk):
        return modelo.objects.filter(nombre__in=lista_nombre_fk)


    def get_objeto_por_id(self, id, modelo):
        return modelo.objects.get(id=id)

    def get_objetos_por_nombres(self, modelo, lista_nombres):
        return modelo.objects.filter(nombre__in=lista_nombres)

    def crear_objeto(self, datos_instancia):
        modelo = datos_instancia.get('modelo')
        objeto = modelo.objects.create(**datos_instancia.get('campos'))

        if not datos_instancia.get('relaciones'):
            return objeto

        for relacion_nm, lista_nombres in datos_instancia.get('relaciones').items():
            getattr(objeto, relacion_nm).set(lista_nombres)

        return objeto

    def modificar_objeto(self, id, modelo, kwargs, datos):

        objeto = self.get_objeto_por_id(id, modelo)

        self.modificar_campos(modelo, objeto, kwargs, datos)

        objeto.save()

        return objeto

    def modificar_campos(self, modelo, objeto, kwargs, datos_fk):
        for campo_modelo in modelo._meta.get_fields():
            if campo_modelo in kwargs:
                setattr(objeto, campo_modelo, kwargs[campo_modelo])
        self.modificar_campos_nm(modelo, objeto,  kwargs, datos_fk)

    def modificar_campos_nm(self, modelo, objeto, kwargs, datos_fk):
        for nombre_relacion, lista_objetos in datos_fk.get('relaciones').items():
            relacion_nm = getattr(objeto, nombre_relacion)
            relacion_nm.set(lista_objetos)







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

        print("CREAR OBJETO")
        modelo = datos_instancia.get('modelo')
        campos = datos_instancia.get('campos')
        relaciones = datos_instancia.get('relaciones')
        print(relaciones)

        objeto = modelo.objects.create(**campos)

        print(f"EN CREAR OBJETO de GESTOR CONSULTAS => ", objeto)

        if not relaciones:
            return objeto

        for relacion_nm, lista_objetos in relaciones.items():
            #dame relacion de este objeto
            relacion = getattr(objeto, relacion_nm)
            #ya tengo la ref, entonces hago el cambio sin indicar explicitamente el objeto
            relacion.set(lista_objetos)

        print("PROBANDO PROBANDO  QUE TENGA TODOS LOS VALORES BIEN ASIGNADOS")
        for field in objeto._meta.fields:
            nombre_campo = field.name
            valor = getattr(objeto, nombre_campo)
            print(f"{nombre_campo}: {valor}")


        return objeto

    def modificar_objeto(self, id, modelo, kwargs, datos):

        objeto = self.get_objeto_por_id(id, modelo)

        self.modificar_campos(modelo, objeto, kwargs, datos)
        print("VISUALIZO MODIFICAR_OBJETOS")
        print(objeto)
        for field in objeto._meta.fields:
            nombre_campo = field.name
            valor = getattr(objeto, nombre_campo)
            print(f"{nombre_campo}: {valor}")

        objeto.save()

        return objeto

    def eliminar_objeto(self, id, modelo):
        return self.get_objeto_por_id(id, modelo).delete()

    def modificar_campos(self, modelo, objeto, kwargs, datos_fk):
        for campo_modelo in modelo._meta.get_fields():
            nombre_campo = campo_modelo.name
            if nombre_campo in kwargs:
                setattr(objeto, nombre_campo, kwargs[nombre_campo] )
        self.modificar_campos_nm(modelo, objeto,  kwargs, datos_fk)

    def modificar_campos_nm(self, modelo, objeto, kwargs, datos_fk):
        for nombre_relacion, lista_objetos in datos_fk.get('relaciones').items():
            getattr(objeto, nombre_relacion).set(lista_objetos)







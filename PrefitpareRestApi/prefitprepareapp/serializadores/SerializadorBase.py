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

    servicio_serializador = ServicioSerializadorBase()
    gestor_consulta = GestorConsulta()

    def obtener_campo_fk(self, campo_fk):
        return self.Meta.model._meta.get_field(campo_fk)

    def es_ingrediente(self):
        return self.Meta.model.__name__ == 'Ingrediente'

    def es_plato(self):
        return self.Meta.model.__name__ == 'Plato'

    def es_modelo_NM(self):
        return self.es_plato() or self.es_ingrediente()

    def crear(self, **kwargs):
        if self.es_modelo_NM():
            lista_categorias = kwargs.pop('categorias')
            if self.es_plato():
                lista_tipos_persona = kwargs.pop('tipos_persona')
                lista_ingredientes = kwargs.pop('ingredientes')

        objeto = self.Meta.model.objects.create(**kwargs)

        if self.es_modelo_NM():
            self.servicio_serializador.asociar_lista_fk(objeto, lista_categorias, Categoria, 'categoria')
            if self.es_plato():
                self.servicio_serializador.asociar_lista_fk(objeto, lista_ingredientes, Ingrediente, 'ingrediente')
                self.servicio_serializador.asociar_lista_fk(objeto, lista_tipos_persona, TipoPersona, 'tipo_persona')

        return objeto

    def modificar(self, id, **kwargs):

        objeto = self.gestor_consulta.get_objeto_por_id(id, self.Meta.model)

        # Cogemos los datos de las N:M
        # TO-DO: Globalizar lógica de generar lista de nombres de las fk a modificar
        if self.es_modelo_NM():
            lista_objetos_nombres_fk = self.servicio_serializador.generar_objetos_nombres_fk(kwargs, 'categorias')
            categorias_instancias = self.gestor_consulta.get_lista_objetos(lista_objetos_nombres_fk, Categoria)
            if self.es_plato():
                lista_objetos_nombres_fk = self.servicio_serializador.generar_objetos_nombres_fk(kwargs, 'tipos_persona')
                tipos_persona_instancias = self.gestor_consulta.get_lista_objetos(lista_objetos_nombres_fk , TipoPersona)
                lista_objetos_nombres_fk = self.servicio_serializador.generar_objetos_nombres_fk(kwargs, 'ingredientes')
                ingredientes_instancias = self.gestor_consulta.get_lista_objetos(lista_objetos_nombres_fk, Ingrediente)

        # Modificamos los campos que no son N:M
        for campo_modelo in self.Meta.fields:
            if campo_modelo in kwargs:
                setattr(objeto, campo_modelo, kwargs[campo_modelo])

        # Efectúamos la modificación de los campos fk N:M
        if self.es_modelo_NM():
            objeto.categoria.set(categorias_instancias)

            if self.es_plato():
                objeto.tipo_persona.set(tipos_persona_instancias)
                objeto.ingrediente.set(ingredientes_instancias)

        objeto.save()

        return objeto

    #TO-DO hacer metodo que acepete un tipo de modelo y devuelva el return de si es ese en cuestion

    def eliminar(self, id):
        self.gestor_consulta.get_objeto_por_id(id, self.Meta.model).delete()













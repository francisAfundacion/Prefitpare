from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from prefitprepareapp.models import  ModeloBase
from prefitprepareapp.models import Categoria
from prefitprepareapp.models import PersonaTipo
from prefitprepareapp.models import Ingrediente


# Agregar comprobacion de existencia de los registros post, put, patch
# Comprobar si no encontrado
# TO-DO => SIMPLIFICAR Y HACERLO MÁS LEGIBLE EL CÓDIGO

class SerializadorBase(serializers.ModelSerializer):

    def crear(self, **kwargs):
        #Optimizable los if y los pop
        if self.es_modelo_NM():
            categorias = self.generar_cuerpo_categorias(kwargs)
            kwargs.pop('categorias', None)

            if self.es_plato():
                lista_tipos_persona = self.generar_cuerpo_personas_tipos(kwargs)
                lista_ingredientes_nombres = self.generar_cuerpo_ingredientes(kwargs)
                # Pensar crear método pop personalizado
                kwargs.pop('tipos_persona', None)
                kwargs.pop('ingredientes', None)

        objeto = self.Meta.model.objects.create(**kwargs)

        if self.es_modelo_NM():
            self.asociar_lista_categorias(objeto, categorias)

            if self.es_plato():
                self.asociar_lista_ingredientes(objeto, lista_ingredientes_nombres)
                self.asociar_lista_personas_tipos(objeto,lista_tipos_persona)

        return objeto


    def modificar(self, id, **kwargs):

        objeto = self.Meta.model.objects.get(id=id)

        # Cogemos los datos de las N:M
        if self.es_modelo_NM():
            categorias_instancias = self.crear_lista_categorias(self.generar_cuerpo_categorias(kwargs))

            if self.es_plato():
                tipos_persona_instancias = self.crear_lista_personas_tipos(self.generar_cuerpo_personas_tipos(kwargs))
                print(tipos_persona_instancias.exists())
                print("Tipos de Persona Instancias:", tipos_persona_instancias)
                ingredientes_instancias =  self.crear_lista_ingredientes(self.generar_cuerpo_ingredientes(kwargs))

        # Modificamos los campos que no son N:M
        for campo_modelo in self.Meta.fields:
            if campo_modelo in kwargs:
                setattr(objeto, campo_modelo, kwargs[campo_modelo])

        # Efectúamos la modificación de los campos fk N:M
        if self.es_modelo_NM():
            objeto.categoria.set(categorias_instancias)

            if self.es_plato():
                print(tipos_persona_instancias.exists())
                for tipo_persona in tipos_persona_instancias:
                    print(tipo_persona.nombre)
                objeto.personaTipo.set(tipos_persona_instancias)
                objeto.ingrediente.set(ingredientes_instancias)

        objeto.save()

        return objeto

    def obtener_campo_fk(self, campo_fk):
        return self.Meta.model._meta.get_field(campo_fk)

    def eliminar(self, id):
        self.Meta.model.objects.get(id=id).delete()

    def crear_lista_categorias(self, cuerpo_categorias_nombres):
        return Categoria.objects.filter(nombre__in=cuerpo_categorias_nombres)

    # Pensar si que siempre me dé una lista y un json en caso que solo tenga una categoría (A futuro)
    # Pensar optimizar los asociar

    ##Pensar en asumir la logica de las consultas con una interfaz e implementación por cada clase o una clase abstracta y una clase implementacion llamada consulta

    def asociar_lista_categorias(self, objeto, categorias):
        categorias_sql = self.crear_lista_categorias(categorias)
        objeto.categoria.set(categorias_sql)

    def generar_cuerpo_categorias(self, kwargs):
        cuerpo_categorias_nombres = [categoria['categoria'] for categoria in kwargs['categorias']]
        return cuerpo_categorias_nombres

    def generar_cuerpo_personas_tipos(self, kwargs):
        cuerpo_personas_tipos = [persona_tipo['tipo_persona'] for persona_tipo in kwargs['tipos_persona']]
        return cuerpo_personas_tipos

    def crear_lista_personas_tipos(self, lista_tipos_persona):
        return PersonaTipo.objects.filter(nombre__in=lista_tipos_persona)

    def asociar_lista_personas_tipos (self, objeto, lista_tipos_persona):
        personas_tipo_sql = self.crear_lista_personas_tipos(lista_tipos_persona)
        objeto.personaTipo.set(personas_tipo_sql)

    def generar_cuerpo_ingredientes(self, kwargs):
        lista_ingredientes_nombres = [ingrediente['ingrediente'] for ingrediente in kwargs['ingredientes']]
        return lista_ingredientes_nombres

    def crear_lista_ingredientes(self, lista_ingredientes_nombres):
        return Ingrediente.objects.filter(nombre__in=lista_ingredientes_nombres)

    def asociar_lista_ingredientes(self, objeto, lista_ingredientes_nombres):
        ingredientes_sql = self.crear_lista_ingredientes(lista_ingredientes_nombres)
        objeto.ingrediente.set(ingredientes_sql)

    # Ver como hace entendinble el primero para que tambien se lea que sea como NM
    # Revisar optimizar las comprobaciones de adelante

    def es_ingrediente(self):
        return self.Meta.model.__name__ == 'Ingrediente'

    def es_plato(self):
        return self.Meta.model.__name__ == 'Plato'

    def es_modelo_NM(self):
        return  self.es_plato() or self.es_ingrediente()






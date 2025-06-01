from prefitprepareapp.infraestructura.GestorConsulta import GestorConsulta
from prefitprepareapp.models import Categoria
from prefitprepareapp.models import TipoPersona
from prefitprepareapp.models import Plato
from prefitprepareapp.models import Ingrediente
from .http import levantar_404_si_falla, levantar_400_si_nombre_vacio


class ServicioSerializadorBase:

    gestor_bd = GestorConsulta()

    RELACIONES_NM = {
        'Plato': ['categorias', 'tipos_persona', 'ingredientes'],
        'Ingrediente': ['categorias'],
    }


    def crear(self, kwargs, modelo):

        relaciones_nm = self.construir_objetos_fk(kwargs, modelo)

        datos_instancia = {
            'modelo': modelo,
            'campos': kwargs,
            'relaciones': relaciones_nm
        }

        return self.gestor_bd.crear_objeto(datos_instancia)

    def modificar(self, id, kwargs, modelo):

        relaciones_nm = self.construir_objetos_fk(kwargs, modelo)

        datos = {
            'modelo': modelo,
            'campos': kwargs,
            'relaciones': relaciones_nm
        }

        return  self.gestor_bd.modificar_objeto(id, modelo, kwargs, datos)

    #modelo._meta.local_many_to_many => filtra automáticamente los campos definidos del modelo
    def construir_objetos_fk(self, kwargs, modelo):

        objetos_relaciones_nm = {}

        for campo_objeto in modelo._meta.local_many_to_many:
                lista_diccionarios = kwargs.pop(campo_objeto.name)
                modelo_relacion = campo_objeto.related_model
                objetos_relaciones_nm[campo_objeto.name] = self.convertir_objetos_fk(
                    modelo_relacion, lista_diccionarios
                )
        return objetos_relaciones_nm
    def convertir_objetos_fk(self, modelo, lista_diccionarios_fk):

        nombres_fk = [diccionario.get('nombre') for diccionario in lista_diccionarios_fk]

        return self.gestor_bd.get_objetos_por_nombres(modelo, nombres_fk)

    def eliminar(self, id, modelo):
        self.gestor_bd.eliminar_objeto(id, modelo)

    def obtener_campo_fk(self, campo_fk):
        return self.Meta.model._meta.get_field(campo_fk)

    def es_ingrediente(self, modelo):
        return modelo == Ingrediente

    def es_plato(self, modelo):
        return modelo == Plato

    def es_modelo_NM(self, modelo):
        return self.es_plato(modelo) or self.es_ingrediente(modelo)

    def conseguir_objetos_modelo(self, modelo):
        return self.gestor_bd.get_objetos(modelo)





from prefitprepareapp.infraestructura.GestorConsulta import GestorConsulta

from prefitprepareapp.models import Categoria
from prefitprepareapp.models import TipoPersona
from prefitprepareapp.models import Plato
from prefitprepareapp.models import Ingrediente


class ServicioSerializadorBase:

    gestor_bd = GestorConsulta()

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
        print("ANTES")
        print(datos)
        print(datos.get('relaciones'))

        for relacion, lista_nombres in datos.get('relaciones').items():
            datos['relaciones'][relacion] = self.obtener_lista_objetos(modelo, lista_nombres)

        print('PRINT DATOS')
        print(datos)

        return  self.gestor_bd.modificar_objeto(id, modelo, kwargs, datos)




    #TO-DO hacer metodo que acepete un tipo de modelo y devuelva el return de si es ese en cuestion

    def eliminar(self, id):
        self.gestor_consulta.get_objeto_por_id(id, self.Meta.model).delete()

    def obtener_campo_fk(self, campo_fk):
        return self.Meta.model._meta.get_field(campo_fk)

    def es_ingrediente(self, modelo):
        return modelo == Ingrediente

    def es_plato(self, modelo):
        return modelo == Plato

    def es_modelo_NM(self, modelo):
        return self.es_plato(modelo) or self.es_ingrediente(modelo)

    def construir_objetos_fk(self, kwargs, modelo):
        print('ESTOY EN CONSTRUIR')
        print(modelo)
        objetos_relaciones_nm = {}

        if self.es_modelo_NM(modelo):
            objetos_relaciones_nm['categoria'] = self.convertir_objetos_fk(modelo, kwargs.pop('categorias'))
            if self.es_plato(modelo):
                objetos_relaciones_nm['tipo_persona'] = self.convertir_objetos_fk(modelo, kwargs.pop('tipos_persona'))
                objetos_relaciones_nm['ingredientes'] = self.convertir_objetos_fk(modelo, kwargs.pop('ingrediente'))

        return objetos_relaciones_nm

    def obtener_lista_objetos(self, modelo, lista_nombres):
        return self.gestor_bd.get_objetos_por_nombres(modelo, lista_nombres)

    def convertir_objetos_fk(self, modelo, lista_dicts_fk):
        nombres_fk = [list(campo_nm.values())[0] for campo_nm in lista_dicts_fk]
        return self.gestor_bd.get_lista_objetos(modelo, nombres_fk)



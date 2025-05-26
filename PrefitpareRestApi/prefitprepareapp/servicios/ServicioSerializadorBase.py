from prefitprepareapp.infraestructura.GestorConsulta import GestorConsulta
from prefitprepareapp.models import Categoria
from prefitprepareapp.models import TipoPersona
from prefitprepareapp.models import Plato
from prefitprepareapp.models import Ingrediente


class ServicioSerializadorBase:

    gestor_bd = GestorConsulta()

    RELACIONES_NM = {
        'Plato': ['categorias', 'tipos_persona', 'ingredientes'],
        'Ingrediente': ['categorias'],
    }

    def crear(self, kwargs, modelo):
        print("EN CREAR")

        relaciones_nm = self.construir_objetos_fk(kwargs, modelo)
        print(" AA PUNTO DE PRINTEAR RELACIONES_NM EN CREAR SERVICIOS")
        print(relaciones_nm)

        datos_instancia = {
            'modelo': modelo,
            'campos': kwargs,
            'relaciones': relaciones_nm
        }
        print(datos_instancia)

        return self.gestor_bd.crear_objeto(datos_instancia)

    def modificar(self, id, kwargs, modelo):
        print("ESTOY EN MODIFICAR DEL SERVICIO")

        relaciones_nm = self.construir_objetos_fk(kwargs, modelo)

        datos = {
            'modelo': modelo,
            'campos': kwargs,
            'relaciones': relaciones_nm
        }
        print("ANTES")
        print(datos)
        print(datos.get('relaciones'))
        print("ESTOY ANTES BUCLE RELACIONES ")
        for relacion in datos.get('relaciones').items():
            print(datos.get(relacion) )

        #for relacion, lista_nombres in datos.get('relaciones').items():
           # datos['relaciones'] = self.obtener_lista_objetos(modelo, lista_nombres)

        print('PRINT DATOS')
        print(datos)

        return  self.gestor_bd.modificar_objeto(id, modelo, kwargs, datos)


    #TO-DO hacer metodo que acepete un tipo de modelo y devuelva el return de si es ese en cuestion

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
    ##aqui peta tengo que ver como montarmela mejor al construir_objeto_fk

    #modelo._meta.local_many_to_many => filtra automaticamente los campos definidos del modelo
    def construir_objetos_fk(self, kwargs, modelo):
        print(modelo)
        print(kwargs)
        objetos_relaciones_nm = {}
        print("CONSTURIR OBEJTOS FK")
        for campo_objeto in modelo._meta.local_many_to_many:
                lista_diccionarios = kwargs.pop(campo_objeto.name)
                print(f"lista diccionarios => ", lista_diccionarios)
                modelo_relacion = campo_objeto.related_model
                print(f"modelo_relacion", modelo_relacion)
                objetos_relaciones_nm[campo_objeto.name] = self.convertir_objetos_fk(
                    modelo_relacion, lista_diccionarios
                )
                print(f"objetos relacion_nm", objetos_relaciones_nm)
        print("VISYALIZO OBJETOS FK")
        print(objetos_relaciones_nm)
        return objetos_relaciones_nm

    def obtener_lista_objetos(self, modelo, lista_nombres):
        return self.gestor_bd.get_objetos_por_nombres(modelo, lista_nombres)

    def convertir_objetos_fk(self, modelo, lista_diccionarios_fk):

        nombres_fk = [diccionario.get('nombre') for diccionario in lista_diccionarios_fk]
        print("VOY A DEVOLVER ALGO EN CONVERTIR_OBJETOS")
        print(nombres_fk)
        print(self.gestor_bd.get_lista_objetos(modelo, nombres_fk))
        return self.gestor_bd.get_lista_objetos(modelo, nombres_fk)






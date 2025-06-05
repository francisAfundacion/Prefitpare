from prefitprepareapp.infraestructura.GestorConsulta import GestorConsulta
from prefitprepareapp.models import Categoria
from prefitprepareapp.models import TipoPersona
from prefitprepareapp.models import Plato
from prefitprepareapp.models import Ingrediente
from .http import levantar_404_si_falla, levantar_400_si_nombre_vacio


class ServicioSerializadorBase:
    """
    Clase que se encarga de preparar los datos para posteriormente interactuar con la base de datos, llamando a la capa
    de infraestructura.

    Recibe la referencia del modelo, la cual determina que secuencia de código ejecutar.

    Atributos:
        gestor_bd (GestorConsulta): Encapsula las interacciones directas con la base de datos.
        RELACIONES_NM (dict): Diccionario que define explícitamente los modelos que tienen relaciones many-to-many relevantes.
    """

    gestor_bd = GestorConsulta()

    RELACIONES_NM = {
        'Plato': ['categorias', 'tipos_persona', 'ingredientes'],
        'Ingrediente': ['categorias'],
    }


    def crear(self, kwargs, modelo):

        """
         Crea una nueva instancia del modelo especificado.

         Parámetros:
             kwargs (dict): Diccionario plano con los datos del nuevo objeto, incluyendo posibles relaciones NM.
             modelo (Model): Referencia al modelo Django sobre el que se va a operar.

         Retorna:
             Model: Instancia del modelo recién creada y persistida.
         """
        relaciones_nm = self.construir_objetos_fk(kwargs, modelo)

        datos_instancia = {
            'modelo': modelo,
            'campos': kwargs,
            'relaciones': relaciones_nm
        }

        return self.gestor_bd.crear_objeto(datos_instancia)

    def modificar(self, id, kwargs, modelo):

        """
            Modifica una instancia existente del modelo especificado.

            Parámetros:
                id (int): Identificador de la instancia a modificar.
                kwargs (dict): Nuevos valores para actualizar la instancia, puede incluir relaciones NM.
                modelo (Model): Referencia al modelo Django sobre el que se va a operar.

            Retorna:
                Model: Instancia del modelo actualizada y persistida.
         """

        relaciones_nm = self.construir_objetos_fk(kwargs, modelo)

        datos = {
            'modelo': modelo,
            'campos': kwargs,
            'relaciones': relaciones_nm
        }

        return  self.gestor_bd.modificar_objeto(id, modelo, kwargs, datos)

    def construir_objetos_fk(self, kwargs, modelo):

        """
            Extrae y construye las relaciones ManyToMany desde los datos entrantes.

            Parámetros:
                kwargs (dict): Datos entrantes, entre los cuales podemos hallar listas de diccionarios representando relaciones NM.
                modelo (Model): Modelo base al que se le extraen sus campos ManyToMany.

            Retorna:
                dict: Diccionario con los campos NM como clave y listas de instancias relacionadas como valor.
        """

        objetos_relaciones_nm = {}

        for campo_objeto in modelo._meta.local_many_to_many:  #filtra automáticamente los campos definidos del modelo
            lista_diccionarios = kwargs.pop(campo_objeto.name, None)

            if lista_diccionarios is not None:  # Solo si viene la relación
                modelo_relacion = campo_objeto.related_model
                objetos_relaciones_nm[campo_objeto.name] = self.convertir_objetos_fk(
                    modelo_relacion, lista_diccionarios
                )

        return objetos_relaciones_nm

    def convertir_objetos_fk(self, modelo, lista_diccionarios_fk):
        """
            Convierte una lista de diccionarios que contiene los campos nombre de las fk N:M en una lista de instancias del modelo relacionado.

            Parámetros:
                modelo (Model): Modelo al que pertenecen los objetos relacionados.
                lista_diccionarios_fk (list): Lista de diccionarios, donde cada uno contiene un campo 'nombre'.

            Retorna:
                list: Lista de instancias del modelo relacionadas.
        """
        nombres_fk = [diccionario.get('nombre') for diccionario in lista_diccionarios_fk]
        return self.gestor_bd.get_objetos_por_nombres(modelo, nombres_fk)

    def eliminar(self, id, modelo):
        """
        Elimina una instancia del modelo dado.

        Parámetros:
            id (int): Identificador del objeto a eliminar.
            modelo (Model): Clase del modelo sobre el que se opera.
        """
        self.gestor_bd.eliminar_objeto(id, modelo)

    def obtener_campo_fk(self, campo_fk):
        """
        Devuelve la definición del campo FK de un modelo.

        Parámetros:
            campo_fk (str): Nombre del campo foráneo.

        Retorna:
            Field: Objeto de campo del modelo.
        """
        return self.Meta.model._meta.get_field(campo_fk)

    def es_ingrediente(self, modelo):
        return modelo == Ingrediente

    def es_plato(self, modelo):
        return modelo == Plato

    def es_modelo_NM(self, modelo):
        return self.es_plato(modelo) or self.es_ingrediente(modelo)

    def conseguir_objetos_modelo(self, modelo):
        """
        Retorna todos los objetos del modelo especificado.

        Parámetros:
            modelo (Model): Clase del modelo.

        Retorna:
            QuerySet: Lista de objetos del modelo.
        """
        return self.gestor_bd.get_objetos(modelo)





from rest_framework.authtoken.models import Token


class GestorConsulta:
    """
    Clase encargada de gestionar las operaciones directas sobre la base de datos para los modelos Django.
    Proporciona métodos para CRUD (Crear, Leer, Actualizar, Eliminar) así como para manejar relaciones many-to-many.

    Esta clase actúa como capa de infraestructura para la persistencia y recuperación de datos.
    """

    def get_objetos(self, modelo):
        return modelo.objects.all()

    def get_objeto_por_id(self, id, modelo):
        return modelo.objects.get(id=id)

    def get_objetos_por_nombres(self, modelo, lista_nombres):
        """
          Obtiene objetos del modelo cuyo campo nombre coincida con alguno en una lista dada.

          Parámetros:
              modelo (Model): Clase del modelo Django.
              lista_nombres (list): Lista de strings con los nombres buscados.

          Retorna:
              QuerySet: Objetos que coinciden con los nombres indicados.
        """
        return modelo.objects.filter(nombre__in=lista_nombres)

    def crear_objeto(self, datos_instancia):
        """
            Crea una nueva instancia de un modelo, incluyendo la asignación de relaciones many-to-many si se proporcionan.

            Parámetros:
                datos_instancia (dict): Diccionario con la siguiente estructura:
                    - 'modelo' (Model): Modelo sobre el que se creará la instancia.
                    - 'campos' (dict): Campos y valores para dar de alta un objeto de un modelo.
                    - 'relaciones' (dict): Relaciones many-to-many, con clave como nombre del campo y valor lista de instancias relacionadas.
            Retorna:
                Model: Instancia creada y persistida en la base de datos.
        """
        modelo = datos_instancia.get('modelo')
        campos = datos_instancia.get('campos')
        relaciones = datos_instancia.get('relaciones')

        objeto = modelo.objects.create(**campos)

        if not relaciones:
            return objeto

        for relacion_nm, lista_objetos in relaciones.items():
            # Dame la relacion de este objeto
            relacion = getattr(objeto, relacion_nm)
            # Ya tengo la ref, entonces hago el cambio sin indicar explícitamente el objeto
            relacion.set(lista_objetos)

        return objeto

    def modificar_objeto(self, id, modelo, kwargs, datos):
        """
            Modifica una instancia existente de un modelo, actualizando sus campos y relaciones.

            Parámetros:
                id (int): ID de la instancia a modificar.
                modelo (Model): Clase del modelo.
                kwargs (dict): Campos y valores a actualizar.
                datos (dict): Diccionario que incluye las relaciones many-to-many para actualizar.

            Retorna:
                Model: Instancia actualizada y guardada.
        """

        objeto = self.get_objeto_por_id(id, modelo)

        self.modificar_campos(modelo, objeto, kwargs, datos)

        objeto.save()

        return objeto

    def eliminar_objeto(self, id, modelo):
        """
          Elimina una instancia del modelo basado en su ID.

          Parámetros:
              id (int): Identificador de la instancia a eliminar.
              modelo (Model): Clase del modelo.

          Retorna: diccionario con detalles del borrado.
        """
        return self.get_objeto_por_id(id, modelo).delete()

    def modificar_campos(self, modelo, objeto, kwargs, datos_fk):
        """
        Actualiza los campos simples y las relaciones many-to-many de una instancia.

        Parámetros:
            modelo (Model): Clase del modelo.
            objeto (Model): Instancia a modificar.
            kwargs (dict): Campos simples y valores a actualizar.
            datos_fk (dict): Diccionario con posibles relaciones many-to-many para actualizar.
        """
        for campo_modelo in modelo._meta.get_fields():
            nombre_campo = campo_modelo.name
            if nombre_campo in kwargs:
                setattr(objeto, nombre_campo, kwargs[nombre_campo] )
        self.modificar_campos_nm(modelo, objeto,  kwargs, datos_fk)

    def modificar_campos_nm(self, modelo, objeto, kwargs,  datos_fk):
        """
            Actualiza las relaciones many-to-many de una instancia.

            Parámetros:
                modelo (Model): Clase del modelo.
                objeto (Model): Instancia a modificar.
                kwargs (dict): Datos recibidos para modificar.
                datos_fk (dict): Diccionario con relaciones many-to-many (clave: nombre relación, valor: lista de instancias).
        """
        relaciones = datos_fk.get('relaciones')
        if relaciones:
            for nombre_relacion, lista_objetos in datos_fk.get('relaciones').items():
                getattr(objeto, nombre_relacion).set(lista_objetos)

    def crear_token(self, instance):
        """
        Crea un token de autenticación para un usuario dado.

        Parámetros:
            instance (User): Instancia de usuario para la cual se crea el token.

        Retorna:
            Token: Token de autenticación creado.
        """
        return Token.objects.create(user=instance)









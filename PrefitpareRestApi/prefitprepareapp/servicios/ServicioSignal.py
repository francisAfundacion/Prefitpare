from prefitprepareapp.infraestructura.GestorConsulta import GestorConsulta


class ServicioSignal:
    """
    Servicio encargado de gestionar operaciones relacionadas con señales del sistema,
    específicamente la creación y manejo de tokens de autenticación para usuarios.

    Atributos:
        gestor_bd (GestorConsulta): Instancia que encapsula las operaciones directas sobre la base de datos,
                                    como la creación de tokens de autenticación.
    """
    gestor_bd = GestorConsulta()

    def gestionar_token(self, instancia):
        """
        Crea un token de autenticación asociado a la instancia de usuario proporcionada.

        Parámetros:
            instancia (User): Instancia del modelo de usuario para la cual se generará el token.

        Retorna:
            Token: Objeto Token creado y asociado al usuario.
        """
        return self.gestor_bd.crear_token(instancia)

from prefitprepareapp.infraestructura.GestorConsulta import GestorConsulta


class ServicioSignal:

    gestor_bd = GestorConsulta()

    def gestionar_token(self, instancia):
        return self.gestor_bd.crear_token(instancia)

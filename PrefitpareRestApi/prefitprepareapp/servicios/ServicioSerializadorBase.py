from prefitprepareapp.infraestructura.GestorConsulta import GestorConsulta

class ServicioSerializadorBase:

    NOMBRES_FK = ["categoria", "tipo_persona", "ingrediente"]
    CAMPOS_WRAP_FK = ["categorias", "tipos_persona", "ingredientes"]

    gestor_consulta = GestorConsulta()

    def asociar_lista_fk(self, objeto, lista_nombres_fk, modelo, campo_relacional):

        lista_objetos_sql = self.gestor_consulta.get_lista_objetos(lista_nombres_fk, modelo)
        getattr(objeto, campo_relacional).set(lista_objetos_sql)

    def generar_objetos_nombres_fk(self, kwargs, wrap_fk):

        mapa_wrap_fk = {
            "categorias": "categoria",
            "tipos_persona": "tipo_persona",
            "ingredientes": "ingrediente"
        }

        clave_fk = mapa_wrap_fk.get(wrap_fk)

        lista_nombres_fk = [ objeto_fk[clave_fk] for objeto_fk in kwargs[wrap_fk] ]

        return lista_nombres_fk








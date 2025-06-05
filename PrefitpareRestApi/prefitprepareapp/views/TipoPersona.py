from rest_framework.views import APIView
from rest_framework.response import Response
from prefitprepareapp.models import TipoPersona
from prefitprepareapp.serializadores.SerializadorTipoPersona import SerializadorTipoPersona
from prefitprepareapp.swaggerEjemplos.tipo_persona import *
from drf_yasg.utils import swagger_auto_schema
from prefitprepareapp.permisos.usuariosPermisos import EsUsuarioConPermisos
from prefitprepareapp.servicios.ServicioSerializadorBase import ServicioSerializadorBase
from prefitprepareapp.servicios.http import levantar_404_si_falla, levantar_400_si_nombre_vacio,  levantar_400_si_integridad_falla


"""
    Punto de entrada de la RestAPI, en la que se delega la petición al serializador correspondiente.
"""
class listarPersonaTipoAPIView(APIView):
    @swagger_auto_schema(**swagger_listar_tipos_persona)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def get(self, request):
        """
               Obtiene la lista de los tipos de persona del sistema, formateada por el serializador correspondiente.

               Parámetros:
                   request (HttpRequest): La solicitud HTTP entrante.

               Retorna:
                   Response: Lista de tipos de persona en formato JSON con código 200.
        """
        servicio = ServicioSerializadorBase()
        serializador_tipo_persona = SerializadorTipoPersona(servicio.conseguir_objetos_modelo(TipoPersona), many=True)
        return Response(serializador_tipo_persona.data)

class crearPersonaTipoAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_crear_tipo_persona)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def post(self, request):
        """
            Crea un nuevo tipo de persona a partir de los datos enviados en la solicitud.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante que contiene los datos,
                                        para dar de alta un nuevo tipo de persona.
            Retorna:
                Response: Mensaje de éxito con el ID del nuevo tipo de persona y código 201.
        """
        serializador_persona_tipo =  SerializadorTipoPersona()
        nuevo_tipo_persona = serializador_persona_tipo.crear(**request.data)
        return Response({'id': nuevo_tipo_persona.id, "mensaje": "Tipo de persona creado con éxito."}, status=201)

class modificarPersonaTipoAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_modificar_tipo_persona)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def put(self, request, id):
        """
            Reemplaza completamente los datos de un tipo de persona existente.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante, contiene los nuevos valores de los campos a modificar.
                id (int): Identificador del tipo de persona a modificar.

            Retorna:
                Response: Detalles del tipo de persona actualizado con código 200.
        """
        return self.modificarAPIView(request, id)
    @swagger_auto_schema(**swagger_modificar_tipo_persona)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def patch(self, request, id):
        """
            Reemplaza parcialmente los datos de un tipo de persona existente.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante, contiene los nuevos valores de los campos a modificar.
                id (int): Identificador del tipo de persona a modificar.

            Retorna:
                Response: Detalles del tipo de persona actualizado con código 200.
        """
        return self.modificarAPIView(request, id)

    def modificarAPIView(self, request, id):
        """
            Método reutilizado por PUT y PATCH para actualizar el tipo de persona.

            Parámetros:
                request (HttpRequest): La solicitud HTTP con datos de actualización.
                id (int): Identificador del tipo de persona  a modificar.

            Retorna:
                Response: Información del tipo de persona actualizado con código 200.
        """
        serializador_persona_tipo =  SerializadorTipoPersona()
        persona_tipo_modif =  serializador_persona_tipo.modificar(id, **request.data)
        return Response({"id": persona_tipo_modif.id, "nombre_nuevo": persona_tipo_modif.nombre, "mensaje":"El tipo de persona ha sido actualizado con éxito."}, status=200)

class eliminarPersonaTipoAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_eliminar_tipo_persona)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def delete(self, request, id):
        """
            Elimina un tipo de persona existente, identificado por su ID.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante.
                id (int): Identificador del tipo de persona a eliminar.

            Retorna:
                Response: Mensaje de éxito con el ID eliminado y código 200.
        """
        serializador_persona_tipo =  SerializadorTipoPersona()
        serializador_persona_tipo.eliminar(id)
        return Response({"id": id, "mensaje": "Tipo de persona eliminado con éxito."})
from rest_framework.views import APIView
from rest_framework.response import Response
from prefitprepareapp.models import Plato
from prefitprepareapp.serializadores.SerializadorPlato import SerializadorPlato
from prefitprepareapp.swaggerEjemplos.plato import *
from drf_yasg.utils import swagger_auto_schema
from prefitprepareapp.permisos.usuariosPermisos import EsUsuarioConPermisos
from prefitprepareapp.servicios.ServicioSerializadorBase import ServicioSerializadorBase
from prefitprepareapp.servicios.http import levantar_404_si_falla, levantar_400_si_nombre_vacio,  levantar_400_si_integridad_falla


"""
    Punto de entrada de la RestAPI, en la que se le delega la petición al serializador correspondiente.
"""
class listarPlatosAPIView(APIView):
    @swagger_auto_schema(**swagger_listar_platos)
    def get(self, request):
        """
            Obtiene la lista de los platos del sistema, formateada por el serializador correspondiente.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante.

            Retorna:
                Response: Lista de platos en formato JSON con código 200.
        """
        servicio = ServicioSerializadorBase()
        serializador_plato = SerializadorPlato(servicio.conseguir_objetos_modelo(Plato), many=True)
        return Response(serializador_plato.data)


class crearPlatoAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_crear_plato)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def post(self, request):
        """
            Crea un nuevo plato a partir de los datos enviados en la solicitud.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante que contiene los datos,
                                        para dar de alta un nuevo plato.
            Retorna:
                Response: Mensaje de éxito con el ID del nuevo plato y código 201.
        """
        serializador_platos = SerializadorPlato()
        nuevo_plato = serializador_platos.crear(**request.data)
        return Response({'id': nuevo_plato.id, "mensaje": "Plato creado con éxito."}, status=201)

class modificarPlatoAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_modificar_plato)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def put(self, request, id):
        """
              Reemplaza completamente los datos de un plato existente.

              Parámetros:
                  request (HttpRequest): La solicitud HTTP entrante, contiene los nuevos valores de los campos a modificar.
                  id (int): Identificador del plato a modificar.

              Retorna:
                  Response: Detalles del plato actualizado con código 200.
        """
        return self.modificarAPIView(request, id)

    @swagger_auto_schema(**swagger_modificar_plato)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def patch(self, request, id):
        """
              Reemplaza parcialmente los datos de un plato existente.

              Parámetros:
                  request (HttpRequest): La solicitud HTTP entrante, contiene los nuevos valores de los campos a modificar.
                  id (int): Identificador del plato a modificar.

              Retorna:
                  Response: Detalles del plato actualizado con código 200.
        """
        return self.modificarAPIView(request, id)

    def modificarAPIView(self, request, id):
        """
            Método reutilizado por PUT y PATCH para actualizar el plato.

            Parámetros:
                request (HttpRequest): La solicitud HTTP con datos de actualización.
                id (int): Identificador del plato a modificar.

            Retorna:
                Response: Información del plato actualizado con código 200.
        """
        serializador_platos = SerializadorPlato()
        plato_modif = serializador_platos.modificar(id, **request.data)
        return Response({"id": plato_modif.id, "nombre_nuevo": plato_modif.nombre, "mensaje":"El plato ha sido actualizado con éxito."})

class eliminarPlatoAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_eliminar_plato)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def delete(self, request, id):
        """
            Elimina un plato existente identificado por su ID.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante.
                id (int): Identificador del plato a eliminar.

            Retorna:
                Response: Mensaje de éxito con el ID eliminado y código 200.
        """
        serializador_platos = SerializadorPlato()
        serializador_platos.eliminar(id)
        return Response({"id": id, "mensaje": "El plato ha sido eliminado con éxito."})


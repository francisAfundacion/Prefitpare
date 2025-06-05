from rest_framework.views import APIView
from rest_framework.response import Response
from prefitprepareapp.models import Ingrediente
from prefitprepareapp.serializadores.SerializadorIngrediente import SerializadorIngrediente
from prefitprepareapp.swaggerEjemplos.ingrediente import *
from drf_yasg.utils import swagger_auto_schema
from prefitprepareapp.permisos.usuariosPermisos import EsUsuarioConPermisos
from prefitprepareapp.servicios.ServicioSerializadorBase import ServicioSerializadorBase
from prefitprepareapp.servicios.http import levantar_404_si_falla, levantar_400_si_nombre_vacio,  levantar_400_si_integridad_falla


"""
    Punto de entrada de la RestAPI, en la que se le delega la petición al serializador correspondiente.
"""
class listarIngredientesAPIView(APIView):
    @swagger_auto_schema(**swagger_listar_ingredientes)
    def get(self, request):
        """
            Obtiene la lista de los ingredientes del sistema, formateada por el serializador correspondiente.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante.

            Retorna:
                Response: Lista de ingredientes en formato JSON con código 200.
        """
        servicio = ServicioSerializadorBase()
        serializador_ingrediente = SerializadorIngrediente(servicio.conseguir_objetos_modelo(Ingrediente), many=True)
        return Response(serializador_ingrediente.data)

class crearIngredienteAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_crear_ingrediente)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def post(self, request):
        """
            Crea un nuevo ingrediente a partir de los datos enviados en la solicitud.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante que contiene los datos,
                                        para dar de alta un nuevo ingrediente.

            Retorna:
                Response: Mensaje de éxito con el ID del nuevo ingrediente y código 201.
        """
        serializador_ingrediente= SerializadorIngrediente()
        nuevo_ingrediente = serializador_ingrediente.crear(**request.data)
        return Response({'id': nuevo_ingrediente.id, "mensaje": "Ingrediente creado con éxito."}, status=201)

class modificarIngredienteAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]

    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    @swagger_auto_schema(**swagger_modificar_ingrediente)
    def put(self, request, id):
        """
            Reemplaza completamente los datos de un ingrediente existente.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante, contiene los nuevos valores de los campos a modificar.
                id (int): Identificador del ingrediente a modificar.

            Retorna:
                Response: Detalles del ingrediente actualizado con código 200.
        """
        return self.modificarAPIView(request, id)

    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    @swagger_auto_schema(**swagger_modificar_ingrediente)
    def patch(self, request, id):
        """
             Reemplaza parcialmente los datos de un ingrediente existente.

             Parámetros:
                 request (HttpRequest): La solicitud HTTP entrante, contiene los nuevos valores de los campos a modificar.
                 id (int): Identificador del ingrediente a modificar.

             Retorna:
                 Response: Detalles del ingrediente actualizado con código 200.
         """
        return self.modificarAPIView(request, id)

    def modificarAPIView(self, request, id):
        """
            Método reutilizado por PUT y PATCH para actualizar el ingrediente.

            Parámetros:
                request (HttpRequest): La solicitud HTTP con datos de actualización.
                id (int): Identificador del ingrediente a modificar.

            Retorna:
                Response: Información del ingrediente actualizado con código 200.
        """
        serializador_ingrediente = SerializadorIngrediente()
        ingrediente_modif =  serializador_ingrediente.modificar(id, **request.data)
        return Response({"id": ingrediente_modif.id, "nombre_nuevo": ingrediente_modif.nombre, "mensaje":"El ingrediente ha sido actualizado con éxito."}, status=200)

class eliminarIngredienteAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_eliminar_ingrediente)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def delete(self, request, id):
        """
            Elimina un ingrediente existente identificado por su ID.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante.
                id (int): Identificador del ingrediente a eliminar.

            Retorna:
                Response: Mensaje de éxito con el ID eliminado y código 200.
        """
        serializador_ingrediente = SerializadorIngrediente()
        serializador_ingrediente.eliminar(id)
        return Response({"id": id, "mensaje": "Ingrediente eliminado con éxito."})
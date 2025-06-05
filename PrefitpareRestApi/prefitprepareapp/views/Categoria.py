from rest_framework.views import APIView
from rest_framework.response import Response
from prefitprepareapp.models import Categoria
from prefitprepareapp.serializadores.SerializadorCategoria import SerializadorCategoria
from prefitprepareapp.swaggerEjemplos.categoria import *
from drf_yasg.utils import swagger_auto_schema
from prefitprepareapp.permisos.usuariosPermisos import EsUsuarioConPermisos
from prefitprepareapp.servicios.ServicioSerializadorBase import ServicioSerializadorBase
from prefitprepareapp.servicios.http import levantar_404_si_falla, levantar_400_si_nombre_vacio,  levantar_400_si_integridad_falla

"""
    Punto de entrada de la RestAPI, en la que se le delega la petición al serializador correspondiente.
"""
class listarCategoriasAPIView(APIView):
    @swagger_auto_schema(**swagger_listar_categorias)
    def get(self, request):
        """
            Obtiene la lista de categorías del sistema, formateada por el serializador correspondiente.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante.

            Retorna:
                Response: Lista de categorías en formato JSON con código 200.
        """
        servicio =  ServicioSerializadorBase()
        serializador_categoria = SerializadorCategoria(servicio.conseguir_objetos_modelo(Categoria), many=True)
        return Response(serializador_categoria.data)

class crearCategoriaAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_crear_categoria)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def post(self, request):
        """
            Crea una nueva categoría a partir de los datos enviados en la solicitud.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante que contiene los datos,
                                       para dar de alta una nueva categoría.

            Retorna:
                Response: Mensaje de éxito con el ID de la nueva categoría y código 201.
        """
        serializador_categoria = SerializadorCategoria()
        nueva_categoria = serializador_categoria.crear(**request.data)
        return Response({'id': nueva_categoria.id, "mensaje": "Categoría creada con éxito."}, status=201)

class modificarCategoriaAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @levantar_400_si_integridad_falla
    @swagger_auto_schema(**swagger_modificar_categoria)
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def put(self, request, id):
        """
            Reemplaza completamente los datos de una categoría existente.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante, contiene los nuevos valores de los campos a modificar.
                id (int): Identificador de la categoría a modificar.

            Retorna:
                Response: Detalles de la categoría actualizada con código 200.
        """
        return self.modificarAPIView(request, id)

    @levantar_400_si_integridad_falla
    @swagger_auto_schema(**swagger_modificar_categoria)
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def patch(self, request, id):
        """
            Cambiar parcialmente los campos de una categoría existente.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante, contiene los nuevos valores de los campos a modificar.
                id (int): Identificador de la categoría a modificar.

            Retorna:
                Response: Detalles de la categoría actualizada con código 200.
        """
        return self.modificarAPIView(request, id)

    def modificarAPIView(self, request, id):
        """
            Método interno reutilizado por PUT y PATCH para actualizar la categoría.

            Parámetros:
                request (HttpRequest): La solicitud HTTP con datos de actualización.
                id (int): Identificador de la categoría a modificar.

            Retorna:
                Response: Información de la categoría actualizada con código 200.
        """
        serializador_categoria = SerializadorCategoria()
        categoria_modif =  serializador_categoria.modificar(id, **request.data)
        return Response({"id": categoria_modif.id, "nombre_nuevo": categoria_modif.nombre, "mensaje":"La categoría ha sido actualizado con éxito."}, status=200)

class eliminarCategoriaAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @levantar_400_si_integridad_falla
    @swagger_auto_schema(**swagger_eliminar_categoria)
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def delete(self, request, id):
        """
            Elimina una categoría existente identificada por su ID.

            Parámetros:
                request (HttpRequest): La solicitud HTTP entrante.
                id (int): Identificador de la categoría a eliminar.

            Retorna:
                Response: Mensaje de éxito con el ID eliminado y código 200.
        """
        serializador_categoria = SerializadorCategoria()
        serializador_categoria.eliminar(id)
        return Response({"id": id, "mensaje": "Categoría eliminada con éxito."})








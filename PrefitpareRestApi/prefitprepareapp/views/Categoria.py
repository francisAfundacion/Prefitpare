from rest_framework.views import APIView
from rest_framework.response import Response
from prefitprepareapp.models import Categoria
from prefitprepareapp.serializadores.SerializadorCategoria import SerializadorCategoria
from prefitprepareapp.swaggerEjemplos.categoria import *
from drf_yasg.utils import swagger_auto_schema
from prefitprepareapp.permisos.usuariosPermisos import EsUsuarioConPermisos

class listarCategoriasAPIView(APIView):
    @swagger_auto_schema(**swagger_listar_categorias)
    def get(self, request):
        lista_categorias = Categoria.objects.all()
        serializador_categoria = SerializadorCategoria(lista_categorias, many=True)
        return Response(serializador_categoria.data)

class crearCategoriaAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_crear_categoria)
    def post(self, request):
        serializador_categoria = SerializadorCategoria()
        nueva_categoria = serializador_categoria.crear(**request.data)
        return Response({'id': nueva_categoria.id, "mensaje": "Categoría creada con éxito."}, status=201)

class modificarCategoriaAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_modificar_categoria)
    def put(self, request, id):
            return self.modificarAPIView(request, id)
    @swagger_auto_schema(**swagger_modificar_categoria)
    def patch(self, request, id):
            return self.modificarAPIView(request, id)

    def modificarAPIView(self, request, id):
        serializador_categoria = SerializadorCategoria()
        categoria_modif =  serializador_categoria.modificar(id, **request.data)
        return Response({"categoria_id": categoria_modif.id, "nombre_nuevo": categoria_modif.nombre, "mensaje":"El producto ha sido actualizado con éxito."}, status=200)

class eliminarCategoriaAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_eliminar_categoria)
    def delete(self, request, id):
        serializador_categoria = SerializadorCategoria()
        serializador_categoria.eliminar(id)
        return Response({"id": id, "mensaje": "Categoría eliminada con éxito."})








from rest_framework.views import APIView
from rest_framework.response import Response
from prefitprepareapp.models import Plato
from prefitprepareapp.serializadores.SerializadorPlato import SerializadorPlato
from prefitprepareapp.swaggerEjemplos.plato import *
from drf_yasg.utils import swagger_auto_schema
from prefitprepareapp.permisos.usuariosPermisos import EsUsuarioConPermisos
from prefitprepareapp.servicios.ServicioSerializadorBase import ServicioSerializadorBase


class listarPlatosAPIView(APIView):
    @swagger_auto_schema(**swagger_listar_platos)
    def get(self, request):
        servicio = ServicioSerializadorBase()
        serializador_plato = SerializadorPlato(servicio.conseguir_objetos_modelo(Plato), many=True)
        return Response(serializador_plato.data)


class crearPlatoAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_crear_plato)
    def post(self, request):
        serializador_platos = SerializadorPlato()
        nuevo_plato = serializador_platos.crear(**request.data)
        return Response({'id': nuevo_plato.id, "mensaje": "Plato creado con éxito."}, status=201)

class modificarPlatoAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_modificar_plato)
    def put(self, request, id):
            return self.modificarAPIView(request, id)
    @swagger_auto_schema(**swagger_modificar_plato)
    def patch(self, request, id):
            return self.modificarAPIView(request, id)

    def modificarAPIView(self, request, id):

        serializador_platos = SerializadorPlato()
        plato_modif = serializador_platos.modificar(id, **request.data)
        return Response({"plato_id": plato_modif.id, "nombre_nuevo": plato_modif.nombre, "mensaje":"El plato ha sido actualizado con éxito."}, status=200)

class eliminarPlatoAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_eliminar_plato)
    def delete(self, request, id):
        serializador_platos = SerializadorPlato()
        serializador_platos.eliminar(id)
        return Response({"id": id, "mensaje": "El plato ha sido eliminado con éxito."})


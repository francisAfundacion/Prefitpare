from rest_framework.views import APIView
from rest_framework.response import Response
from prefitprepareapp.models import Ingrediente
from prefitprepareapp.serializadores.SerializadorIngrediente import SerializadorIngrediente
from prefitprepareapp.swaggerEjemplos.ingrediente import *
from drf_yasg.utils import swagger_auto_schema
from prefitprepareapp.permisos.usuariosPermisos import EsUsuarioConPermisos
from prefitprepareapp.servicios.ServicioSerializadorBase import ServicioSerializadorBase
from prefitprepareapp.servicios.http import levantar_404_si_falla, levantar_400_si_nombre_vacio,  levantar_400_si_integridad_falla



class listarIngredientesAPIView(APIView):
    @swagger_auto_schema(**swagger_listar_ingredientes)
    def get(self, request):
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
            return self.modificarAPIView(request, id)

    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    @swagger_auto_schema(**swagger_modificar_ingrediente)
    def patch(self, request, id):
            return self.modificarAPIView(request, id)

    def modificarAPIView(self, request, id):
        serializador_ingrediente = SerializadorIngrediente()
        categoria_modif =  serializador_ingrediente.modificar(id, **request.data)
        return Response({"categoria_id": categoria_modif.id, "nombre_nuevo": categoria_modif.nombre, "mensaje":"El ingrediente ha sido actualizado con éxito."}, status=200)

class eliminarIngredienteAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_eliminar_ingrediente)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def delete(self, request, id):
        serializador_ingrediente = SerializadorIngrediente()
        serializador_ingrediente.eliminar(id)
        return Response({"id": id, "mensaje": "Ingrediente eliminado con éxito."})
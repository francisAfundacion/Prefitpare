from rest_framework.views import APIView
from rest_framework.response import Response
from prefitprepareapp.models import TipoPersona
from prefitprepareapp.serializadores.SerializadorTipoPersona import SerializadorTipoPersona
from prefitprepareapp.swaggerEjemplos.tipo_persona import *
from drf_yasg.utils import swagger_auto_schema
from prefitprepareapp.permisos.usuariosPermisos import EsUsuarioConPermisos
from prefitprepareapp.servicios.ServicioSerializadorBase import ServicioSerializadorBase
from prefitprepareapp.servicios.http import levantar_404_si_falla, levantar_400_si_nombre_vacio,  levantar_400_si_integridad_falla



class listarPersonaTipoAPIView(APIView):
    @swagger_auto_schema(**swagger_listar_tipos_persona)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def get(self, request):
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
            return self.modificarAPIView(request, id)
    @swagger_auto_schema(**swagger_modificar_tipo_persona)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def patch(self, request, id):
            return self.modificarAPIView(request, id)

    def modificarAPIView(self, request, id):
        serializador_persona_tipo =  SerializadorTipoPersona()
        persona_tipo_modif =  serializador_persona_tipo.modificar(id, **request.data)
        return Response({"categoria_id": persona_tipo_modif.id, "nombre_nuevo": persona_tipo_modif.nombre, "mensaje":"El tipo de persona ha sido actualizado con éxito."}, status=200)

class eliminarPersonaTipoAPIView(APIView):
    permission_classes = [EsUsuarioConPermisos]
    @swagger_auto_schema(**swagger_eliminar_tipo_persona)
    @levantar_400_si_integridad_falla
    @levantar_400_si_nombre_vacio
    @levantar_404_si_falla
    def delete(self, request, id):
        serializador_persona_tipo =  SerializadorTipoPersona()
        serializador_persona_tipo.eliminar(id)
        return Response({"id": id, "mensaje": "Tipo de persona eliminado con éxito."})
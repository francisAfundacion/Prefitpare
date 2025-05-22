from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from prefitprepareapp.models import TipoPersona
from prefitprepareapp.serializadores.SerializadorTipoPersona import SerializadorTipoPersona
import datetime

class listarPersonaTipoAPIView(APIView):
    def get(self, request):
        lista_personas_tipos = TipoPersona.objects.all()
        serializador_persona_tipo = SerializadorTipoPersona(lista_personas_tipos, many=True)
        return Response(serializador_persona_tipo.data)

class crearPersonaTipoAPIView(APIView):
    def post(self, request):
        serializador_persona_tipo =  SerializadorTipoPersona()
        nuevo_tipo_persona = serializador_persona_tipo.crear(**request.data)
        return Response({'id': nuevo_tipo_persona.id, "mensaje": "Tipo de persona creado con éxito."}, status=201)

class modificarPersonaTipoAPIView(APIView):
    def put(self, request, id):
            return self.modificarAPIView(request, id)

    def patch(self, request, id):
            return self.modificarAPIView(request, id)

    def modificarAPIView(self, request, id):
        serializador_persona_tipo =  SerializadorTipoPersona()
        persona_tipo_modif =  serializador_persona_tipo.modificar(id, **request.data)
        return Response({"categoria_id": persona_tipo_modif.id, "nombre_nuevo": persona_tipo_modif.nombre, "mensaje":"El tipo de persona ha sido actualizado con éxito."}, status=200)

class eliminarPersonaTipoAPIView(APIView):
    def delete(self, request, id):
        serializador_persona_tipo =  SerializadorTipoPersona()
        serializador_persona_tipo.eliminar(id)
        return Response({"id": id, "mensaje": "Tipo de persona eliminado con éxito."})
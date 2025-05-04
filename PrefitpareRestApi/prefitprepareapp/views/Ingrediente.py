from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from prefitprepareapp.models import Ingrediente
from prefitprepareapp.serializadores.SerializadorIngrediente import SerializadorIngrediente
import datetime

class listarIngredientesAPIView(APIView):
    def get(self, request):
        lista_ingredientes = Ingrediente.objects.all()
        serializador_ingrediente = SerializadorIngrediente(lista_ingredientes, many=True)
        return Response(serializador_ingrediente.data)

class crearIngredienteAPIView(APIView):
    def post(self, request):
        serializador_ingrediente= SerializadorIngrediente()
        nuevo_ingrediente = serializador_ingrediente.crear(**request.data)
        return Response({'id': nuevo_ingrediente.id, "mensaje": "Ingrediente creado con éxito."}, status=201)

class modificarIngredienteAPIView(APIView):
    def put(self, request, id):
            return self.modificarAPIView(request, id)

    def patch(self, request, id):
            return self.modificarAPIView(request, id)

    def modificarAPIView(self, request, id):
        serializador_ingrediente = SerializadorIngrediente()
        categoria_modif =  serializador_ingrediente.modificar(id, **request.data)
        return Response({"categoria_id": categoria_modif.id, "nombre_nuevo": categoria_modif.nombre, "mensaje":"El ingrediente ha sido actualizado con éxito."}, status=200)

class eliminarIngredienteAPIView(APIView):
    def delete(self, request, id):
        serializador_ingrediente = SerializadorIngrediente()
        serializador_ingrediente.eliminar(id)
        return JsonResponse({"id": id, "mensaje": "Ingrediente eliminada con éxito."})
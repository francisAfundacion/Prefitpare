from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from prefitprepareapp.models import Plato
from prefitprepareapp.serializadores.SerializadorPlato import SerializadorPlato
import datetime

class listarPlatosAPIView(APIView):
    def get(self, request):
        lista_platos = Plato.objects.all()
        serializador_platos = SerializadorPlato(lista_platos, many=True)
        return Response(serializador_platos.data)

class crearPlatoAPIView(APIView):
    def post(self, request):
        serializador_platos = SerializadorPlato()
        nuevo_plato = serializador_platos.crear(**request.data)
        return Response({'id': nuevo_plato.id, "mensaje": "Plato creado con éxito."}, status=201)

class modificarPlatoAPIView(APIView):
    def put(self, request, id):
            return self.modificarAPIView(request, id)

    def patch(self, request, id):
            return self.modificarAPIView(request, id)

    def modificarAPIView(self, request, id):
        serializador_platos = SerializadorPlato()
        plato_modif= serializador_platos.modificar(id, **request.data)
        return Response({"plato_id": plato_modif.id, "nombre_nuevo": plato_modif.nombre, "mensaje":"El plato ha sido actualizado con éxito."}, status=200)

class eliminarPlatoAPIView(APIView):
    def delete(self, request, id):
        serializador_platos = SerializadorPlato()
        serializador_platos.eliminar(id)
        return Response({"id": id, "mensaje": "El plato ha sido eliminado con éxito."})

"""
    categoria = models.ManyToManyField(Categoria)
    personaTipo = models.ManyToManyField(PersonaTipo)
    peso = models.DecimalField(max_digits=3, decimal_places=2) #Campo decimal 2.23 => kg
    origenPais = models.CharField(max_length=40)
"""
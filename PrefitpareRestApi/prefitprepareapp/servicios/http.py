from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError


def levantar_404_si_falla(vista_func):
    @wraps(vista_func)
    def wrapper(*args, **kwargs):
        try:
            return vista_func(*args, **kwargs)
        except ObjectDoesNotExist:
            raise Http404("No existe el recurso/s solicitado/s acorde al id especificado")
    return wrapper

def levantar_400_si_nombre_vacio(view_func):
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        nombre = request.data.get('nombre')
        if nombre is not None and str(nombre).strip() == "":
            return Response({"error": "El campo 'nombre' no puede estar vacío."}, status=status.HTTP_400_BAD_REQUEST)
        return view_func(self, request, *args, **kwargs)
    return wrapper

def levantar_400_si_integridad_falla(view_func):
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        try:
            return view_func(self, request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"error": "Error de integridad de datos. Es probable que ya exista un registro con el mismo nombre."},
                status=status.HTTP_400_BAD_REQUEST
            )
    return wrapper
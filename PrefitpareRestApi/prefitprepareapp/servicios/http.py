from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError


def levantar_404_si_falla(vista_func):
    """
    Decorador que controla la excepción ObjectDoesNotExist al lanzar la función decorada. En consecuencia retorna una
    respuesta HTTP 404 si no se ha encontrado el recurso deseado en la base de datos.

     Parámetros:
        vista_func (callable): La función de la vista original en la que puede saltar la excepción ObjectDoesNotExist.
        Recibe como argumentos self, request como primeros argumentos.
        También se incluyen *args y **kwargs porque la función a la que se le aplica este decorador los emplea.
        Si no se agregan, el decorador fallaría al ejecutarse, ya que no estaría pasando todos los argumentos necesarios.

     Retorna:
        callable: La misma función decorada. En caso de error, lanza Http404, lo cual produce una respuesta HTTP 404 gestionada por el framework.
                  En caso contrario sigue con normalidad el flujo del código.
     """
    @wraps(vista_func)
    def wrapper(*args, **kwargs):
        try:
            return vista_func(*args, **kwargs)
        except ObjectDoesNotExist:
            raise Http404("No existe el recurso/s solicitado/s acorde al id especificado")
    return wrapper

def levantar_400_si_nombre_vacio(view_func):
    """
      Decorador que comprueba si el campo nombre del cuerpo de la petición llega vacío.
      En caso afirmativo, retorna una respuesta HTTP 400, indicando al usuario que no puede dejar ese campo vacío.

      Parámetros:
        view_func (callable): Función de vista basada en clases que recibe self y request como primeros argumentos.
        También se incluyen *args y **kwargs porque la función a la que se le aplica este decorador los emplea.
        Si no se agregan, el decorador fallaría al ejecutarse, ya que no se estaría pasando todos los argumentos necesarios.

      Retorna:
          callable: La función decorada que retorna una Response con error 400 si nombre está vacío,
                    o continúa normalmente si la validación pasa.
      """
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        nombre = request.data.get('nombre')
        if nombre is not None and str(nombre).strip() == "":
            return Response({"error": "El campo 'nombre' no puede estar vacío."}, status=status.HTTP_400_BAD_REQUEST)
        return view_func(self, request, *args, **kwargs)
    return wrapper

def levantar_400_si_integridad_falla(view_func):
    """
    Descripción:
        Decorador que captura excepciones IntegrityError, lanzados cuando hay conflictos de restricciones en campos
        que deben de contemplar valores únicos.
        Retorna una respuesta HTTP 400 con un mensaje informativo.

    Parámetros:
        view_func (callable): Función de vista que realiza operaciones que pueden violar restricciones de integridad.
        También se incluyen *args y **kwargs, porque son empleados por la función en la que es aplicada el decorador.
        Si no se agregan, el decorador fallaría al ejecutarse, ya que no se estaría pasando todos los argumentos necesarios.


    Retorna:
        callable: La función decorada que retorna una Response con error 400 si ocurre una IntegrityError,
                  o continúa normalmente si no hay errores.
    """
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
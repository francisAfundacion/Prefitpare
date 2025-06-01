from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from functools import wraps

def levantar_404_si_falla(vista_func):
    @wraps(vista_func)
    def wrapper(*args, **kwargs):
        try:
            return vista_func(*args, **kwargs)
        except ObjectDoesNotExist:
            raise Http404("No existe el recurso/s solicitado/s acorde al id especificado")
    return wrapper
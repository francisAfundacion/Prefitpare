from rest_framework.permissions import BasePermission

class EsUsuarioConPermisos(BasePermission):
    """
        Permiso genérico que permite el acceso solo a usuarios autenticados con roles válidos.
    """
    def has_permission(self, request, view):
        return presenta_permisos(request)

class EsAsesor(BasePermission):
    """
        Permisos específicos para usuarios con rol de asesor.
    """
    def has_permission(self, request, view):
        return presenta_permisos(request)

class EsAdmin(BasePermission):
    """
        Permisos específicos para usuarios con rol de admin.
    """
    def has_permission(self, request, view):
        return presenta_permisos(request)

def presenta_permisos(request):
    """
      Verifica si el usuario está autenticado y tiene un rol autorizado.

      Parámetros: request: petición http.

      Retorna:
          bool: True si el usuario tiene un rol permitido ("asesor" o "admin"), False en caso contrario.
      """
    return request.user.is_authenticated and request.user.rol in ["asesor", "admin"]



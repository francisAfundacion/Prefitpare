from rest_framework.permissions import BasePermission

class EsUsuarioConPermisos(BasePermission):
    def has_permission(self, request, view):
        return presenta_permisos(request)

class EsAsesor(BasePermission):
    def has_permission(self, request, view):
        return presenta_permisos(request)

class EsAdmin(BasePermission):
    def has_permission(self, request, view):
        return presenta_permisos(request)

def presenta_permisos(request):
    return request.user.is_authenticated and request.user.rol in ["asesor", "admin"]



"""
URL configuration for PrefitpareRestApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from prefitprepareapp.views.Categoria import *
from prefitprepareapp.views.Ingrediente import *
from prefitprepareapp.views.TipoPersona import *
from prefitprepareapp.views.Plato import *



schema_view = get_schema_view(
    openapi.Info(
        title="API Documentación",
        default_version="v1",
        description="Documentación de la API",
    ),
    public=True,
    permission_classes=[AllowAny],
)
#Agregar get detalle para cada clase

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/categorias', listarCategoriasAPIView.as_view(), name='listar-categorias'),
    path('crear/categoria', crearCategoriaAPIView.as_view(), name='crear-categoria'),
    path('modificar/categoria/<int:id>', modificarCategoriaAPIView.as_view(), name='modificar-categoria'),
    path('eliminar/categoria/<int:id>', eliminarCategoriaAPIView.as_view(), name='eliminar-categoria'),
    path('listar/ingredientes', listarIngredientesAPIView.as_view(), name='listar-ingredientes'),
    path('crear/ingrediente', crearIngredienteAPIView.as_view(), name='crear-ingrediente'),
    path('modificar/ingrediente/<int:id>', modificarIngredienteAPIView.as_view(), name='modificar-ingrediente'),
    path('eliminar/ingrediente/<int:id>', eliminarIngredienteAPIView.as_view(), name='eliminar-ingrediente'),
    path('listar/tipo/personas', listarPersonaTipoAPIView.as_view(), name='listar-tipos-personas'),
    path('crear/tipo/persona', crearPersonaTipoAPIView.as_view(), name='crear-tipo-persona'),
    path('modificar/tipo/persona/<int:id>', modificarPersonaTipoAPIView.as_view(), name='modificar-tipo-persona'),
    path('eliminar/tipo/persona/<int:id>', eliminarPersonaTipoAPIView.as_view(), name='eliminar-tipo-persona'),
    path('listar/platos', listarPlatosAPIView.as_view(), name='listar-platos'),
    path('crear/plato', crearPlatoAPIView.as_view(), name='crear-plato'),
    path('modificar/plato/<int:id>', modificarPlatoAPIView.as_view(), name='modificar-plato'),
    path('eliminar/plato/<int:id>', eliminarPlatoAPIView.as_view(), name='eliminar-plato'),
]

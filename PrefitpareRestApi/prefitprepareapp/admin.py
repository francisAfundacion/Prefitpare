from django.contrib import admin
from prefitprepareapp.models import Plato, Ingrediente, TipoPersona, Categoria, UsuarioPersonalizado

admin.site.register(UsuarioPersonalizado)
admin.site.register(Ingrediente)
admin.site.register(TipoPersona)
admin.site.register(Categoria)
admin.site.register(Plato)

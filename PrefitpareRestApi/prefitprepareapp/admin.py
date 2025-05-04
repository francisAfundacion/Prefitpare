from django.contrib import admin
from prefitprepareapp.models import Plato, Ingrediente, PersonaTipo, Categoria, UsuarioPersonalizado

admin.site.register(UsuarioPersonalizado)
admin.site.register(Ingrediente)
admin.site.register(PersonaTipo)
admin.site.register(Categoria)
admin.site.register(Plato)


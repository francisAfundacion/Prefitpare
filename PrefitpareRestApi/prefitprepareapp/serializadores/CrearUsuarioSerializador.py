#Importar el serializador para  crear usuario y le damos el nombre Base, para poder personalizarlo mediante herencia
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from prefitprepareapp.models import UsuarioPersonalizado

class CrearUsuarioSerializador(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = UsuarioPersonalizado
        fields = (
            'id', 'username', 'email', 'password',
            'nombre', 'telefono', 'rol', 'imagen_perfil'
        )
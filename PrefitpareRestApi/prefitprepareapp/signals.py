from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from prefitprepareapp.servicios.ServicioSignal import ServicioSignal



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
       Señal que se ejecuta automáticamente tras guardar un usuario definido en AUTH_USER_MODEL.
       Cuando el usuario es creado. Se delega la creación del token de autenticación al ServicioSignal.

       Parámetros:
           sender (Model): Modelo que envía la señal, en este caso el modelo de usuario.
           instance (User): Instancia del usuario que se ha guardado.
           created (bool): Indica si la instancia fue creada (True) o simplemente actualizada (False).
    """
    if created:
        servicio_signal = ServicioSignal()
        servicio_signal.gestionar_token(instance)
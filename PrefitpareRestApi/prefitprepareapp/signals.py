from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from prefitprepareapp.servicios.ServicioSignal import ServicioSignal



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        servicio_signal = ServicioSignal()
        servicio_signal.gestionar_token(instance)
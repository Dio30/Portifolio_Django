from django.db.models.signals import post_save
from .models import Cliente
from django.contrib.auth.models import User

def cria_usuario(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(usuario=instance)
    else:
        if not hasattr(instance, "cliente"):
            Cliente.objects.create(usuario=instance)
    
post_save.connect(cria_usuario, sender=User)
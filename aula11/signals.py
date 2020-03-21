from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Automovel
from django.utils.text import slugify

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        UserProfile.objects.create(user=user)

@receiver(post_delete, sender=User)
def send_email(sender, instance, **kwargs):
    user = instance
    print(f"Muito obrigado {user.username} por ter participado da plataforma")

@receiver(pre_save, sender=Automovel)
def slugify_automovel(sender, instance, **kwargs):
    auto = instance
    auto.slug = slugify(f"{auto.marca} {auto.modelo}")
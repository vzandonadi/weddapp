from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Guests(models.Model):

    GODPARENTS_YESNO = (
        (True, 'Sim'),
        (False, 'Não'),
    )
    whatsapp_number = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    is_godparents = models.BooleanField(choices=GODPARENTS_YESNO)

    def __str__(self):
        return (self.last_name, self.first_name)


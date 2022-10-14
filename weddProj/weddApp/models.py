from email.policy import default
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

class Groups(models.Model):
#The group where the groom or the bride knows the person.
    group_name = models.CharField(max_length = 40, unique=True, blank = False, null = False)
    description_group = models.CharField(max_length = 640)

    def __str__(self):
        return (self.group_name)

class Guests(models.Model):

    GODPARENTS_YESNO = (
        (True, 'S'),
        (False, 'N'),
    )
    ISCONFIRMED=(
        ('O', 'N/I'),
        ('Y', 'SIM'),
        ('N', 'NÃO'),
    )
    whatsapp_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=60)
    midle_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60)
    is_godparents = models.BooleanField(default=False, choices=GODPARENTS_YESNO)
    is_confirmed = models.CharField(max_length=1, default='O', choices=ISCONFIRMED)
    group_belongs = models.ForeignKey(Groups, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return (self.first_name + " " + self.last_name)

class GroupMsg(models.Model):
    MSG_TYPES = (
        ('O', 'Comum'),
        ('I', 'Informações'),
        ('N', 'Novidades'),
        ('A', 'Alertas'),
    )
    msg_from = models.ForeignKey(Guests, on_delete = models.CASCADE, blank = False, null = False)
    msg_to = models.ForeignKey(Groups, on_delete = models.CASCADE, blank = False, null = False)
    msg_subject = models.CharField(max_length = 120, blank = False)
    msg_type = models.CharField(max_length = 1, default = 'O', choices = MSG_TYPES)
    msg_body = models.CharField(max_length = 5000)
    msg_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return (self.msg_subject)

class IndividualMsg(models.Model):
    MSG_TYPES = (
        ('O', 'Comum'),
        ('I', 'Informações'),
        ('N', 'Novidades'),
        ('A', 'Alertas'),
    )
    msg_from = models.ForeignKey(Guests, on_delete = models.CASCADE, related_name = 'sender', blank = False, null = False)
    msg_to = models.ForeignKey(Guests, on_delete = models.CASCADE, related_name = 'receiver', blank = False, null = False)
    msg_subject = models.CharField(max_length = 120, blank = False)
    msg_type = models.CharField(max_length = 1, default = 'O', choices = MSG_TYPES)
    msg_body = models.CharField(max_length = 5000)
    msg_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return (self.msg_subject)

class Confirmed(models.Model):
#List of quantity of confirmed people.

    RELATIONSHIP = (
        ('SELF','Convidado'),
        ('PARENTS', 'Pais'),
        ('RELATIVES', 'Familiares'),
        ('CHILDRENS', 'Filho(a)'),
        ('FRIENDS', 'Amigo(a)'),
        ('PARTNER', 'Parceiro(a)/Companheiro(a)')
    )

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    relationship = models.CharField(max_length = 10, choices = RELATIONSHIP)
    who_confirmed = models.ForeignKey(Guests, on_delete = models.CASCADE)
    group_belongs = models.ForeignKey(Groups, on_delete = models.CASCADE, blank = True, null = True)
    date_confirmed = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return (self.first_name)

class AppVersion(models.Model):
#actual version of the app

    version = models.IntegerField()
    version_description = models.CharField(max_length=60)
    released_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return (self.version_description)

class PushToken(models.Model):
#data for push token for each user

    guest = models.ForeignKey(Guests, on_delete = models.CASCADE, blank = False, null = False)
    token = models.CharField(max_length=60)
    created_date = models.DateTimeField(auto_now_add = True)

    # def __str__(self):
    #     return (self.guest)
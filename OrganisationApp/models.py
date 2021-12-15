from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import uuid
from coreApp.models import BaseModel


class Employe(User, BaseModel):
    telephone = models.CharField(max_length=255, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    is_never_connected = models.BooleanField(default=True)
    is_allowed = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to="stockage/images/employes/", max_length=255,  null=True, blank=True)
    brut = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first_name+" "+self.last_name

    def name(self):
        return self.first_name+" "+self.last_name


######################################################################################################
# SIGNAUX


@receiver(pre_save, sender=Employe)
def pre_save_employe(sender, instance, **kwargs):
    if instance._state.adding:
        if instance.username == "":
            instance.username = str(uuid.uuid4()).split("-")[-1]
        if instance.brut == "" or instance.brut is None:
            instance.brut = str(uuid.uuid4()).split("-")[-1]
        instance.set_password(instance.brut)


@receiver(post_save, sender=Employe)
def post_save_employe(sender, instance, created, **kwargs):
    if created:
        pass
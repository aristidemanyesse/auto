
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import Sum, Avg
from coreApp.models import BaseModel, Etat
import uuid
import datetime
import traceback



class Boutique(BaseModel):
    name = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    rate = models.IntegerField(default=0)
    is_official = models.BooleanField(default=False)
    logo = models.ImageField(
        max_length=255, upload_to="stockage/images/boutiques/", default="", null=True, blank=True)
    background = models.ImageField(
        max_length=255, upload_to="stockage/images/boutiques/", default="", null=True, blank=True)
    
    

class Vendeur(BaseModel):
    name = models.CharField(max_length=255)
    etiquette = models.CharField(max_length=255, null=True, blank=True)
    boutique = models.ForeignKey(
        Boutique, on_delete=models.CASCADE, related_name="boutique_vendeur")

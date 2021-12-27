from django.db import models

from coreApp.models import BaseModel

# Create your models here.

class Fournisseur(BaseModel):
    name = models.CharField(max_length=255)
    etiquette = models.CharField(max_length=255, null=True, blank=True)


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
    
    

class Livreur(BaseModel):
    name = models.CharField(max_length=255)
    etiquette = models.CharField(max_length=255, null=True, blank=True)
    boutique = models.ForeignKey(
        Boutique, on_delete=models.CASCADE, related_name="boutique_vendeur")

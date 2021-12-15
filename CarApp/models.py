
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import Sum, Avg
from coreApp.models import BaseModel, Etat
from ShopApp.models import Boutique



class Marque(BaseModel):
    name = models.CharField(max_length=255)


class Modele(BaseModel):
    name = models.CharField(max_length=255)
    year = models.IntegerField(default=0)
    marque = models.ForeignKey(
        Marque, on_delete=models.CASCADE, related_name="marque_modele")


class Transmission(BaseModel):
    name = models.CharField(max_length=255)

class Energie(BaseModel):
    name = models.CharField(max_length=255)

class TypeVehicule(BaseModel):
    name = models.CharField(max_length=255)


class Vehicule(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    modele = models.ForeignKey(
        Modele, on_delete=models.CASCADE, related_name="modele_vehicule")
    couleur = models.CharField(max_length=255, default="")
    puissance = models.IntegerField(default=0)
    portes = models.IntegerField(default=0)
    places = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    cylindres = models.IntegerField(default=0)
    vitesse = models.IntegerField(default=0)
    is_occasion = models.BooleanField(default=False)
    type = models.ForeignKey(
        TypeVehicule, on_delete=models.CASCADE, related_name="type_vehicule")
    energie = models.ForeignKey(
        Energie, on_delete=models.CASCADE, related_name="energie_vehicule")
    transmission = models.ForeignKey(
        Transmission, on_delete=models.CASCADE, related_name="transmission_vehicule")
    boutique = models.ForeignKey(
        Boutique, on_delete=models.CASCADE, related_name="boutique_vehicule")
    image1 = models.ImageField(
        max_length=255, upload_to="stockage/images/pieces/", default="", null=True, blank=True)
    image2 = models.ImageField(
        max_length=255, upload_to="stockage/images/pieces/", default="", null=True, blank=True)
    image3 = models.ImageField(
        max_length=255, upload_to="stockage/images/pieces/", default="", null=True, blank=True)
    image4 = models.ImageField(
        max_length=255, upload_to="stockage/images/pieces/", default="", null=True, blank=True)

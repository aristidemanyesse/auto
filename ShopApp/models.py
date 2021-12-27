
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import Sum, Avg
from FournisseurApp.models import Boutique
from coreApp.models import BaseModel, Etat
import uuid
import datetime
import traceback


class Category(BaseModel):
    name = models.CharField(max_length=255)

class Produit(BaseModel):
    reference = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    is_occasion = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_produit")
    boutique = models.ForeignKey(
        Boutique, on_delete=models.CASCADE, related_name="boutique_produit")
    image1 = models.ImageField(
        max_length=255, upload_to="stockage/images/produits/", default="", null=True, blank=True)
    image2 = models.ImageField(
        max_length=255, upload_to="stockage/images/produits/", default="", null=True, blank=True)
    image3 = models.ImageField(
        max_length=255, upload_to="stockage/images/produits/", default="", null=True, blank=True)
    image4 = models.ImageField(
        max_length=255, upload_to="stockage/images/produits/", default="", null=True, blank=True)


class TypeDuree(BaseModel):
    name = models.CharField(max_length=255)
    days = models.IntegerField(default=0)
    
    
class Garantie(BaseModel):
    produit = models.CharField(max_length=255)
    type_duree = models.IntegerField(default=0)
    
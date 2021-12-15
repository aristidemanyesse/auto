
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import Sum, Avg
from ShopApp.models import Boutique
from coreApp.models import BaseModel, Etat


class CategoryPiece(BaseModel):
    name = models.CharField(max_length=255)


class Piece(BaseModel):
    reference = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    is_occasion = models.BooleanField(default=False)
    category = models.ForeignKey(
        CategoryPiece, on_delete=models.CASCADE, related_name="category_piece")
    boutique = models.ForeignKey(
        Boutique, on_delete=models.CASCADE, related_name="boutique_piece")
    image1 = models.ImageField(
        max_length=255, upload_to="stockage/images/pieces/", default="", null=True, blank=True)
    image2 = models.ImageField(
        max_length=255, upload_to="stockage/images/pieces/", default="", null=True, blank=True)
    image3 = models.ImageField(
        max_length=255, upload_to="stockage/images/pieces/", default="", null=True, blank=True)
    image4 = models.ImageField(
        max_length=255, upload_to="stockage/images/pieces/", default="", null=True, blank=True)

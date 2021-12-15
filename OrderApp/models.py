from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import datetime, uuid
from django.db.models import Sum, Avg

from coreApp.models import BaseModel, Etat
from ItemApp.models import Piece
# Create your models here.


class Commande(BaseModel):
    montant        = models.FloatField(default = 0)
    avance         = models.FloatField(default = 0)
    taux_tva       = models.FloatField(default = 0)
    tva            = models.FloatField(default = 0)
    employe        = models.ForeignKey("OrganisationApp.Employe", on_delete = models.CASCADE, related_name="employe_commande")
    comment        = models.TextField(default="",  null = True, blank=True);

    datelivraison  = models.DateField(null = True, blank=True,)
    acompte_client = models.FloatField(default = 0)
    dette_client   = models.FloatField(default = 0)
    class Meta:
        ordering = ['deleted', "-created_at"]


    @staticmethod
    def chiffre_affaire(agence):
        total = Commande.objects.filter(deleted = False, agence = agence).aggregate(Sum("montant"))
        return total["montant__sum"] or 0


    def __str__(self):
        return "Commande N°"+str(self.id)



class LigneCommande(BaseModel):
    commande = models.ForeignKey(Commande, on_delete = models.CASCADE, related_name="commande_ligne")
    piece   = models.ForeignKey("ItemApp.Piece", on_delete = models.CASCADE, related_name="piece_lignecommande")
    quantite = models.IntegerField(default = 0)
    price    = models.IntegerField(default = 0)


    def __str__(self):
        return str(self.quantite) + " " +self.piece.name+" à " +str(self.price)


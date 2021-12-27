from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import datetime, uuid
from django.db.models import Sum, Avg

from coreApp.models import BaseModel, Etat
# Create your models here.




class TypeClient(BaseModel):
    PARTICULIER = "PARTICULIER"
    ENTREPRISE = "ENTREPRISE"

    name           = models.CharField(max_length = 255, null = True, blank=True)
    etiquette = models.CharField(max_length = 255, null = True, blank=True)


class Client(BaseModel):
    name        = models.CharField(max_length = 255, null = False, blank=False)
    adresse         = models.CharField(max_length = 255, null = True, blank=True)
    email            = models.EmailField(max_length = 255, null = True, blank=True)
    contact         = models.CharField(max_length = 255, null = True, blank=True)
    acompte_initial = models.IntegerField(default=0, null = True, blank=True)
    dette_initial   = models.IntegerField(default=0, null = True, blank=True)
    seuil_credit    = models.IntegerField(default=0, null = True, blank=True)
    type            = models.ForeignKey(TypeClient, on_delete = models.CASCADE, related_name="type_client")


    # def acompte_actuel(self):
    #     total = 0
    #     datas = self.client_compte.filter(mouvement__type__etiquette = TypeMouvement.DEPOT).aggregate(Sum("mouvement__montant"))
    #     total += datas["mouvement__montant__sum"] or 0
    #     datas = self.client_compte.filter(mouvement__type__etiquette = TypeMouvement.RETRAIT).aggregate(Sum("mouvement__montant"))
    #     total -= datas["mouvement__montant__sum"] or 0
    #     return (self.acompte_initial or 0) + total


    # def dette_totale(self):
    #     total = 0
    #     for commande in Commande.objects.filter(groupecommande__client = self, deleted = False):
    #         total += commande.reste_a_payer()

    #     datas = self.client_compte.filter(is_dette = True, mouvement__type__etiquette = TypeMouvement.RETRAIT).aggregate(Sum("mouvement__montant"))
    #     total -= datas["mouvement__montant__sum"] or 0
    #     return (self.dette_initial or 0) + total


    # @staticmethod
    # def dette_clients(agence):
    #     total = 0
    #     for client in Client.objects.filter(deleted = False, agence = agence):
    #         total += client.dette_totale()
    #     return total


    # def get_groupecommandes(self):
    #     return self.client_groupecommande.filter(client = self).exclude(etat__etiquette = Etat.ANNULE).order_by("etat__etiquette", "-created_at", "datelivraison")





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
    piece   = models.ForeignKey("ShopApp.Piece", on_delete = models.CASCADE, related_name="piece_lignecommande")
    quantite = models.IntegerField(default = 0)
    price    = models.IntegerField(default = 0)


    def __str__(self):
        return str(self.quantite) + " " +self.piece.name+" à " +str(self.price)


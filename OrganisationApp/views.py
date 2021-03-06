import datetime
from django.shortcuts import render
from django.http import  JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
from django.shortcuts import render
from productionApp.models import Brique, Ressource
from clientApp.models import Client
from django.contrib.auth import authenticate
# Create your views here.



def home(request):
    datas = {
        "nb_users" : Employe.objects.filter( deleted=False).count(),
        "nb_clients" : Client.objects.filter( deleted=False).count(),
        "nb_briques" : Brique.objects.filter(active = True, deleted=False).count(),
        "agences" : Agence.objects.filter( deleted=False),
    }
    return render(request, "master/pages/home.html", datas)



def dashboard_boutique(request):
    datas = {}
    briques = Brique.objects.filter(active = True, deleted = False)
    for brique in briques:
        data = {
            "attente" : int(brique.attente(request.agence)),
            "livrable" : int(brique.livrable(request.agence)),
            "commande" : int(brique.commande(request.agence)),
        }
        datas[brique] = data

    demain = request.now + datetime.timedelta(days=1)
    context = {
        "datas" : datas,
        "dette_clients" : Client.dette_clients(request.agence),
        "entree_du_jour" :request.agence_compte.total_entree(request.now.date(), demain),
        "depense_du_jour" : request.agence_compte.total_sortie(request.now.date(), demain),
        "solde_actuel" : request.agence_compte.solde_actuel(),
        "rupture_stock_brique" : Brique.en_rupture(request.agence)
    }

    return render(request, "boutique/pages/dashboard.html", context)




def dashboard_fabrique(request):
    datas = {}
    datas_ressources = {}
    for brique in Brique.objects.filter(active = True, deleted = False):
        data = {
            "attente" : int(brique.attente(request.agence)),
            "livrable" : int(brique.livrable(request.agence)),
            "commande" : int(brique.commande(request.agence)),
        }
        datas[brique] = data

    for ressource in Ressource.objects.filter(active = True, deleted = False):
        data = {
            "stock" : ressource.stock(request.agence),
        }
        datas_ressources[ressource] = data



    context = {
        "datas" : datas,
        "datas_ressources" : datas_ressources
    }

    return render(request, "fabrique/pages/dashboard.html", context)




def dashboard_manager(request):
    datas = {}
    datas_ressources = {}
    for brique in Brique.objects.filter(active = True, deleted = False):
        data = {
            "attente" : int(brique.attente(request.agence)),
            "livrable" : int(brique.livrable(request.agence)),
            "commande" : int(brique.commande(request.agence)),
        }
        datas[brique] = data



    for ressource in Ressource.objects.filter(active = True, deleted = False):
        data = {
            "stock" : ressource.stock(request.agence),
        }
        datas_ressources[ressource] = data



    context = {
        "datas" : datas,
        "datas_ressources" : datas_ressources
    }

    return render(request, "manager/pages/dashboard.html", context)


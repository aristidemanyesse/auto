from django.core.management.base import BaseCommand, CommandError
from CarApp.models import Marque, MarqueBatterie, MarquePneu, Modele, TypeMoteur
from settings import settings
import json, os

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        path = os.path.join(settings.BASE_DIR, "coreApp/management/commands/database/batterie") 
        with open(path) as fichier:
            print("Enregistrement des marques de batteries")
            for line in fichier:
                name = line.replace('\n', "")
                print("--------------", name)
                MarqueBatterie.objects.create(
                    name=name
                )

        path = os.path.join(settings.BASE_DIR, "coreApp/management/commands/database/pneu") 
        with open(path) as fichier:
            print("Enregistrement des marques de pneus")
            for line in fichier:
                name = line.replace('\n', "")
                print("--------------", name)
                MarquePneu.objects.create(
                    name=name
                )
                                
        path = os.path.join(settings.BASE_DIR, "coreApp/management/commands/database/type_moteur") 
        with open(path) as fichier:
            print("Enregistrement des types de moteurs")
            for line in fichier:
                name = line.replace('\n', "")
                print("--------------", name)
                TypeMoteur.objects.create(
                    name=name
                )
                
        path = os.path.join(settings.BASE_DIR, "coreApp/management/commands/database/marque_modele.json") 
        with open(path) as fichier:
            print("Enregistrement des marques et des modèles de véhicules")
            data = json.load(fichier)
            for key in data:
                print("--------------", key)
                marque = Marque.objects.create(
                    name=key
                )
                for value in data[key]:
                    print("--------------------------", value)
                    Modele.objects.create(
                        name=value,
                        marque = marque
                    )


    # import ficheApp.bootstrap as app
    # app.run()

    # import comptabilityApp.bootstrap as app
    # app.run()

    # self.stdout.write(self.style.SUCCESS(
    #     'Base de données initialisée avec succes !'))

import time
import json
import os
import sys
from datetime import datetime
from modele.mesure import Mesure

class Controleur:
    def __init__(self, platine, vue):
        self.platine = platine
        self.vue = vue
        self.actif = False #Etat du programme
        self.fichier_json = "donnees.json"

    def demarrer(self):
        self.vue.afficher_message("Pret", "Appuyez Start")
        while True:
            #Si le bouton start est presse
            if self.platine.est_bouton_start_enfonce():
                #On attend que le bouton soit relâché
                while self.platine.est_bouton_start_enfonce():
                    time.sleep(0.1)

                #Systeme inactif
                self.actif = not self.actif

                if self.actif:
                    self.vue.afficher_demarrage() #Message de demarrage fait
                    self.boucle_systeme() #Lance la boucle de mesure
                else:
                    self.vue.afficher_arret() #Message d'arret fait
                    sys.exit() #Quitte le programme
            time.sleep(0.1)

    def boucle_systeme(self):
        #Deboguage
        print("[DEBUG] Attente du bouton Mesure")
        while not self.platine.est_bouton_mesure_enfonce():
            time.sleep(0.1)
        #Deboguage
        print("[DEBUG] Bouton Mesure détecté !")

        #Attendre que le bouton soit relâché
        while self.platine.est_bouton_mesure_enfonce():
            time.sleep(0.1)
        #Deboguage
        print("[DEBUG] Bouton Mesure relâché !")

        while self.actif:
            #Si on appui a nouveau sur le bouton start, on arrete le systeme
            if self.platine.est_bouton_start_enfonce():
                while self.platine.est_bouton_start_enfonce():
                    time.sleep(0.1)
                self.actif = False
                self.vue.afficher_arret()
                sys.exit()

            #Lecture du capteur
            distance = self.platine.lire_distance() #Distance en m
            potentiometre = self.platine.lire_potentiometre() #Potentiometre en %
            #Affichage sur l ecran LCDs
            self.vue.afficher_distance_et_pot(distance, potentiometre)
            #Enregistrement dans le fichier json
            self.sauvegarder_mesure(distance, potentiometre)

            #Attend 5 secondes avant de relancer la mesure
            for _ in range(50):
                #Verifiie si le bouton start est enfonce pendant l attente
                if self.platine.est_bouton_start_enfonce():
                    while self.platine.est_bouton_start_enfonce():
                        time.sleep(0.1)
                    self.actif = False
                    self.vue.afficher_arret()
                    sys.exit()
                time.sleep(0.1)


    def sauvegarder_mesure(self, distance, potentiometre):
        #Date et heure
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #Instance de la classe mesure
        mesure = Mesure(date, [round(distance, 2), round(potentiometre, 2)])

        #Ancienne donnees
        data = self.charger_donnees()
        #Ajout de la mesure
        data.append({
            "date": date,
            "distance_cm": round(distance, 2),
            "potentiometre_val": round(potentiometre, 2)
        })

        #Sauvegarde dans le fichier json
        with open(self.fichier_json, 'w') as f:
            json.dump(data, f, indent=4)

    def charger_donnees(self):
        #Verifier si le fchier existe deja
        if os.path.exists(self.fichier_json):
            with open(self.fichier_json, 'r') as f:
                return json.load(f)
        return []

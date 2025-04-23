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
        self.actif = False
        self.fichier_json = "donnees.json"

    def demarrer(self):
        self.vue.afficher_message("Pret", "Appuyez Start")
        while True:
            if self.platine.est_bouton_start_enfonce():
                while self.platine.est_bouton_start_enfonce():
                    time.sleep(0.1)
                self.actif = not self.actif

                if self.actif:
                    self.vue.afficher_demarrage()
                    self.boucle_systeme()
                else:
                    self.vue.afficher_arret()
                    sys.exit()
            time.sleep(0.1)

    def boucle_systeme(self):
        print("[DEBUG] Attente du bouton Mesure")
        while not self.platine.est_bouton_mesure_enfonce():
            time.sleep(0.1)
        print("[DEBUG] Bouton Mesure détecté !")

        while self.platine.est_bouton_mesure_enfonce():
            time.sleep(0.1)
        print("[DEBUG] Bouton Mesure relâché !")

        while self.actif:
            if self.platine.est_bouton_start_enfonce():
                while self.platine.est_bouton_start_enfonce():
                    time.sleep(0.1)
                self.actif = False
                self.vue.afficher_arret()
                sys.exit()

            distance = self.platine.lire_distance()
            potentiometre = self.platine.lire_potentiometre()
            self.vue.afficher_distance_et_pot(distance, potentiometre)
            self.sauvegarder_mesure(distance, potentiometre)

            for _ in range(50):
                if self.platine.est_bouton_start_enfonce():
                    while self.platine.est_bouton_start_enfonce():
                        time.sleep(0.1)
                    self.actif = False
                    self.vue.afficher_arret()
                    sys.exit()
                time.sleep(0.1)


    def sauvegarder_mesure(self, distance, potentiometre):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mesure = Mesure(date, [round(distance, 2), round(potentiometre, 2)])

        data = self.charger_donnees()
        data.append({
            "date": date,
            "distance_cm": round(distance, 2),
            "potentiometre_val": round(potentiometre, 2)
        })

        with open(self.fichier_json, 'w') as f:
            json.dump(data, f, indent=4)

    def charger_donnees(self):
        if os.path.exists(self.fichier_json):
            with open(self.fichier_json, 'r') as f:
                return json.load(f)
        return []

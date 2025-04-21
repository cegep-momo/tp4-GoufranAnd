import LCD1602
import time

class VueLCD:
    def __init__(self):
        LCD1602.init(0x27, 1) # Initialisation de l'écran LCD
        LCD1602.clear()

    def afficher_message(self, ligne1="", ligne2=""):
        LCD1602.clear()
        LCD1602.write(0, 0, ligne1[:16])
        LCD1602.write(0, 1, ligne2[:16])

    def afficher_distance(self, distance_cm):
        self.afficher_message(f"Distance: {distance_cm:.1f} cm")

    def afficher_mesure_prise(self,valeur):
        self.afficher_message(f"Mesure prise: {valeur:.1f} cm")

    def afficher_demarrage(self):
        self.afficher_message("Demarrage...")
        time.sleep(2)

    def afficher_arret(self):
        self.afficher_message("Arret...")
        time.sleep(2)
        LCD1602.clear()
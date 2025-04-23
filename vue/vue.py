import LCD1602
import time

class VueLCD:
    def __init__(self):
        LCD1602.init(0x27, 1) # Initialisation de l'écran LCD
        LCD1602.clear()


    #Methode de base pour ecrire deux lignes sur l'ecran LCD
    def afficher_message(self, ligne1="", ligne2=""):
        LCD1602.clear()
        LCD1602.write(0, 0, ligne1[:16]) #Ligne 1 position 0
        LCD1602.write(0, 1, ligne2[:16]) #Ligne 2 postion 0

    #affiche la distance sur la premiere ligne
    def afficher_distance(self, distance_cm):
        self.afficher_message(f"Distance: {distance_cm:.1f} cm")

    #Affiche un message que la mesure a ete prise
    def afficher_mesure_prise(self,valeur):
        self.afficher_message(f"Mesure prise: {valeur:.1f} cm")

    #Affiche un message de demarrage
    def afficher_demarrage(self):
        self.afficher_message("Demarrage fait", "Appuyez Mesurer")
        time.sleep(2)

    #Affiche un message d arret    
    def afficher_arret(self):
        self.afficher_message("Arret fait")
        time.sleep(2)
        LCD1602.clear()

    #Affiche la distance(ligne 1) et la valeur du potentiometre(ligne 2)
    def afficher_distance_et_pot(self, distance_cm, pourcentage):
        self.afficher_message(f"Dist: {distance_cm:.1f}cm", f"Pot: {pourcentage:.1f}%")

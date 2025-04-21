from gpiozero import Button, DistanceSensor
import ADC0832

class Platine:
    def __init__(self):
        self.bouton_demarrer = Button(26)
        self.bouton_mesure = Button(19)
        self.capteur = DistanceSensor(echo=17, trigger=14, max_distance=2.0)
        ADC0832.setup()

    def lire_distance(self):
        return self.capteur.distance * 100 #convertit de m en cm
    
    def lire_potentiometre(self):
        valeur = ADC0832.getResult()
        return round((valeur / 255.0) * 100, 2) #Echelle en pourcentage
    
    def est_bouton_demarrer_enfonce(self):
        return self.bouton_demarrer.is_pressed
    
    def est_bouton_mesure_enfonce(self):
        return self.bouton_mesure.is_pressed
    
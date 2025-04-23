from gpiozero import Button, DistanceSensor
from ADCDevice import ADS7830  
 
class Platine:
    def __init__(self):
        self.bouton_demarrer = Button(26)
        self.bouton_mesure = Button(19)
        self.capteur = DistanceSensor(echo=17, trigger=4)  
 
        self.adc = ADS7830()
        if not self.adc.detectI2C(0x4b): 
            print("[DEBUG] Vérifie la connexion I2C.")
 
    def lire_distance(self):
        try:
            return self.capteur.distance * 100  # m → cm
        except:
            return 0.0  # retourne 0 si aucun écho
 
    def lire_potentiometre(self):
        valeur = self.adc.analogRead(0)
        return round((valeur / 255.0) * 100, 2)
 
    def est_bouton_start_enfonce(self):
        return self.bouton_demarrer.is_pressed
 
    def est_bouton_mesure_enfonce(self):
        return self.bouton_mesure.is_pressed
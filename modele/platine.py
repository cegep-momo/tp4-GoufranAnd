from gpiozero import Button, DistanceSensor
from ADCDevice import ADS7830  
class Platine:
    def __init__(self):
        # Initialisation des broches GPIO
        self.bouton_demarrer = Button(26) #Bouton demarrer
        self.bouton_mesure = Button(19) #Bouton mesure
        self.capteur = DistanceSensor(echo=17, trigger=4)  #Capteur de distance
 
        self.adc = ADS7830() #Convertissuer (ADC)
        if not self.adc.detectI2C(0x4b):
            print("Vérifie la connexion I2C.")
 
    def lire_distance(self):
        try:
            return self.capteur.distance * 100  # m → cm
        except:
            return 0.0  # retourne 0 si aucun écho
 
    def lire_potentiometre(self):
        valeur = self.adc.analogRead(0) #Resultat entre 0 et 255
        return round((valeur / 255.0) * 100, 2) #Conversion en porucentage (0-100%)
 
 
    #Retourne true si le bouton start est enfonce
    def est_bouton_start_enfonce(self):
        return self.bouton_demarrer.is_pressed
 
    #Retourne true si le bouton mesure est enfonce
    def est_bouton_mesure_enfonce(self):
        return self.bouton_mesure.is_pressed
 
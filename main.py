from modele.platine import Platine
from vue.vue import VueLCD
from controleur.controleur import Controleur
 
if __name__ == "__main__":
    platine = Platine()
    vue = VueLCD()
    controleur = Controleur(platine, vue)
    controleur.demarrer()
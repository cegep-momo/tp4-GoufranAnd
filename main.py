from modele.platine import Platine
from vue.vue import VueLCD
from controleur.controleur import Controleur
 
if __name__ == "__main__":
    platine = Platine() # Initialisation de la platine
    vue = VueLCD() # Initialisation de la vue
    controleur = Controleur(platine, vue) # Initialisation du controleur
    controleur.demarrer() # Démarrage du programme
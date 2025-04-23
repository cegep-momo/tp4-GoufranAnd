class Mesure:
    def __init__(self, dateHeureMesure, dateMesure):
        self.dateHeureMesure = dateHeureMesure # Date et heure de la mesure
        self.dateMesure = dateMesure # Liste des mesures (valeurs)


    #Retourne une representation lisble de l objet Mesure
    def __repr__(self):
        return f"{self.dateHeureMesure} - {self.dateMesure}"
    
    #Retourne les attributs de l objet sur une ou plusieurs lignes
    def afficherMesure(self):
        texte = f"Date: {self.dateHeureMesure}\n"
        for i,val, in enumerate(self.dateMesure):
            texte += f"Mesure {i+1}: {val}\n"
        return texte

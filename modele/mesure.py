class Mesure:
    def __init__(self, dateHeureMesure, dateMesure):
        self.dateHeureMesure = dateHeureMesure
        self.dateMesure = dateMesure

    def __repr__(self):
        return f"{self.dateHeureMesure} - {self.dateMesure}"
    
    def afficherMesure(self):
        texte = f"Date: {self.dateHeureMesure}\n"
        for i,val, in enumerate(self.dateMesure):
            texte += f"Mesure {i+1}: {val}\n"
        return texte

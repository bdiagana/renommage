from Regle import *
class ListeRegle:

    def __init__(self,regles):
        self.regles=regles

    def getRegles(self):
        return self.regles

    def setRegles(self,newRegles):
        self.regles=newRegles

    def charger(self, nomF):
        with open(nomF, "r") as f:
                return f.read()
        f.close()

    def sauvegarder(self,nomF,nomR):
        fichier = open(nomF, "a")
        fichier.write(nomR+' '+self.regles.__str__()+"\r\n")
        fichier.close()

    def __str__(self):
        return self.regles


from Action import*
class Regle:
    def __init__(self, ammmorce, aPartirDe, prefixe, nomFichier, postfixe,extension=[]):
        self.ammorce=ammmorce
        self.aPartirDe=aPartirDe
        self.prefixe=prefixe
        self.nomFichier=nomFichier
        self.postfixe=postfixe
        self.extension=extension

    def getAmmorce(self):
        return self.ammorce

    def getApartirDe(self):
        return self.aPartirDe

    def getPrefixe(self):
        return self.prefixe

    def getNomfichier(self):
        return self.nomFichier

    def getPostfixe(self):
        return self.postfixe

    def getExtension(self):
        return self.extension

    def ajouteDesZeros(self,nombre,nombreZero):
        nombreStr = str(nombre)
        while len(nombreStr) < nombreZero:
            nombreStr = "0" + nombreStr
        return nombreStr

    def setAmmorce(self,newAmmorce):
        self.ammorce=newAmmorce

    def setApartirDe(self,newAPartirDe):
        self.aPartirDe=newAPartirDe

    def setPrefixe(self,newPrefixe):
        self.prefixe=newPrefixe

    def setNomFichier(self,newNomFichier):
        self.setNomFichier=newNomFichier

    def setPostfixe(self,newPostfixe):
        self.postfixe=newPostfixe

    def setExtension(self,newExtension):
        self.extension=newExtension

    def __str__(self):
        return self.ammorce+' '+self.aPartirDe+' '+self.prefixe+' '+str(self.nomFichier)+' '+self.postfixe+' '+str(self.extension)












import re
import os
from Regle import *
class Action:
    '''
    Constructeur de ma class Action
    '''
    def __init__(self,nomDuRepertoire,regle):
        self.nomDuRepertoire=nomDuRepertoire
        self.regle=regle


    def getNomDuRepertoire(self):
        return self.nomDuRepertoire

    def getRegle(self):
        return self.regle

    def setNomDuRepertoire(self,newNom):
        self.nomDuRepertoire=newNom

    def setRegle(self,newRegle):
        self.regle=newRegle

    def next_letter(self,letters, index):
        letter = letters[index]
        if letter == 'Z':
            result = 'A'
            if index == len(letters) - 1:
                return result + 'A'
            else:
                return result + self.next_letter(letters, index + 1)
        else:
            result = chr(ord(letter) + 1)
            return result + letters[index + 1:]

    '''
    Méthode permettant de simuler un renommage en  affichant les fichiers renommer
    '''

    def simule(self):
        fichier=self.regle.getNomfichier()
        ammorce=self.regle.getAmmorce()
        extension=self.regle.getExtension()
        prefixe=self.regle.getPrefixe()
        postfixe=self.regle.getPostfixe()
        aPartirDe=self.regle.getApartirDe()
        if(fichier == True):
            if(ammorce == 'Chiffre'):
                i = int(aPartirDe)
                for element in os.listdir(self.nomDuRepertoire):
                   for j in range(len(extension)):
                     if element.endswith(extension[j]):
                        ammorce=self.regle.ajouteDesZeros(i,3)
                        elmnt = element.split('.')
                        if prefixe !='aucun' and postfixe!='aucun':
                            fichier=ammorce+prefixe+elmnt[0]+postfixe+'.'+elmnt[1]
                        elif prefixe!='aucun':
                            fichier = ammorce + prefixe + element
                        elif postfixe !='aucun':
                            fichier=ammorce+elmnt[0]+postfixe+'.'+elmnt[1]
                        else:
                            fichier = ammorce + element
                        print(fichier)
                        #os.rename(self.nomDuRepertoire+element,fichier) a mettre dans rennomer
                        i+=1
            elif(ammorce =='Lettre'):
                if(aPartirDe=='aucun'):
                    aPartirDe='A'
                letter=aPartirDe

                for element in os.listdir(self.nomDuRepertoire):
                    for j in range(len(extension)):
                        if element.endswith(extension[j]):
                            letter = self.next_letter(letter[::-1], 0)[::-1]
                            elmnt = element.split('.')
                            if prefixe != 'aucun' and postfixe != 'aucun':
                                file = letter + prefixe+elmnt[0]+postfixe+'.'+elmnt[1]

                            elif prefixe != 'aucun':
                                file=letter+prefixe+element

                            elif postfixe != 'aucun':
                                file=letter+elmnt[0]+postfixe+'.'+elmnt[1]
                            else:
                                file= letter+element
                            print(file)
            else:
                for element in os.listdir(self.nomDuRepertoire):
                    for j in range(len(extension)):
                        if element.endswith(extension[j]):
                            elmnt = element.split('.')
                            if prefixe != 'aucun' and postfixe != 'aucun':
                                file = prefixe + elmnt[0] + postfixe + '.' + elmnt[1]

                            elif prefixe != 'aucun':
                                file =  prefixe + element

                            elif postfixe != 'aucun':
                                file =  elmnt[0] + postfixe + elmnt[1]
                            else:
                                file = element
                            print(file)
        else:
            if(ammorce == 'Chiffre'):
                i = int(aPartirDe)
                for element in os.listdir(self.nomDuRepertoire):
                    for j in range(len(extension)):
                        if element.endswith(extension[j]):
                            ammorce = self.regle.ajouteDesZeros(i, 3)
                            if prefixe !='aucun' and postfixe !='aucun':
                                file = str(ammorce) + prefixe+fichier + postfixe + '.' + extension[j]
                            elif prefixe != 'aucun':
                                file=str(ammorce)+prefixe+fichier+'.'+extension[j]
                            elif postfixe !='aucun':
                                file = str(ammorce) +fichier +postfixe+'.' + extension[j]

                            else:
                                file = str(ammorce) + fichier + '.' + extension[j]
                            #os.rename(self.nomDuRepertoire + element,self.nomDuRepertoire+file)
                            print(file)
                            i += 1
            elif (ammorce == 'Lettre'):
                if(aPartirDe=='aucun'):
                    aPartirDe='A'
                letter=aPartirDe
                for element in os.listdir(self.nomDuRepertoire):
                    for j in range(len(extension)):
                        if element.endswith(extension[j]):
                            letter = self.next_letter(letter[::-1], 0)[::-1]
                            if prefixe != 'aucun' and postfixe != 'aucun':
                                file = letter + prefixe + fichier+ postfixe + '.' + extension[j]

                            elif prefixe != 'aucun':
                                file = letter + fichier+'.'+extension[j]

                            elif postfixe != 'aucun':
                                file = letter + fichier + postfixe + extension[j]
                            else:
                                file = letter + fichier + '.'+ extension[j]
                            print(file)
            else:
                for element in os.listdir(self.nomDuRepertoire):
                    for j in range(len(extension)):
                        if element.endswith(extension[j]):
                            elmnt = element.split('.')
                            if prefixe != 'aucun' and postfixe != 'aucun':
                                file = prefixe + elmnt[0] + postfixe + '.' + elmnt[1]

                            elif prefixe != 'aucun':
                                file =  prefixe + element

                            elif postfixe != 'aucun':
                                file =  elmnt[0] + postfixe + elmnt[1]
                            else:
                                file = element
                            print(file)

    def __str__(self):
        return self.nomDuRepertoire+' '+self.regle

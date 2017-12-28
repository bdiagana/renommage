from Regle import *
'''
Me permet de faire mes test
'''

from Renommage import *
from ListeRegle import*


list=['txt','docx']


r1=Regle('Chiffre','B','aucun',True,'aucun',list)
a1=Action('C:/Users/dsbq5660/PycharmProjects/renommage/',r1)
l1=ListeRegle(r1)


r1 = Regle('Chiffre', '4', '_prefixe', 'test', ' _post', ['txt', 'docx'])
a1 = Renommage('C:/Users/dsbq5660/Documents/files', r1)
a1.renommer()








#for element in os.listdir('C:/Users/dsbq5660/PycharmProjects/renommage/'):
#    if element.endswith(list[i]):
#        print(element)



import os
list_fic = []
for i in range(1, 101):
    list_fic.append('fic' + str(i))
print(list_fic)

def amorce_nombre(liste):
    return [f"{n+1:03d}{liste[n]}" for n in range(0, len(liste))] #liste_amorce

print(amorce_nombre(list_fic))


import random

#Páros számok
def parosak(lista):
    parosSzamok=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            parosSzamok.append(lista[i])
    return parosSzamok


#Páratlan számok 
def paratlanOsszeg(lista):
    paratlanOsszeg = 0
    for i in range(len(lista)):
        if lista[i]%2!=0:
            paratlanOsszeg+=lista[i]
    return paratlanOsszeg
import random


#Számok meg a kiíratás
def Szamjegyek(list):
    for i in range(0,9):
        Szamjegyek = []
        for elem in list:
            szam = str(elem)
            if szam[0]==str(i+1):
                Szamjegyek.append(szam)
        print("Ennyi darab",i+1,"-es/-as/-os számmal kezdődő szám van a listában:",len(Szamjegyek))


szamok = []
randomSzam = 0
for i in range(500):
    randomSzam = random.randint(10000,99999)
    szamok.append(randomSzam)

print("Páros számok száma:",len(parosak(szamok)))
print("Páratlan számok összesen:",paratlanOsszeg(szamok))

#Lista Két része
elsoResz=0
masodikResz=0
for i in range(len(szamok)):
    if i<250:
        elsoResz+=szamok[i]
    else:
        masodikResz+=szamok[i]
if elsoResz > masodikResz:
    print("Az lista első részének összege a nagyobb!")
elif elsoResz < masodikResz:
    print("Az lista második részének összege a nagyobb!")
elif elsoResz == masodikResz:
    print("A lista egyik részének összege és másik részének összege egyenlő")

Szamjegyek(szamok)

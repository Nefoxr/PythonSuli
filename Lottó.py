import random

#otoslotto
otosLista=[]

while len(otosLista)<= 4:
    randomSzam = random.randint(1,90)
    if randomSzam not in otosLista:
        otosLista.append(randomSzam)

print (otosLista)

#hatoslotto
hatosLista=[]

while len(hatosLista)<= 5:
    randomSzam = random.randint(1,45)
    if randomSzam not in hatosLista:
        hatosLista.append(randomSzam)

print (hatosLista)

#skandinavlotto

skandinavLista=[]

while len(skandinavLista)<= 6:
    randomSzam = random.randint(1,35)
    if randomSzam not in skandinavLista:
        skandinavLista.append(randomSzam)

print (skandinavLista)


#toto

toto=["1","2","x"]

while len(skandinavLista)<= 13:
    randomSzam = random.randint(1,12)
    if randomSzam not in skandinavLista:
        skandinavLista.append(randomSzam)

print (skandinavLista)

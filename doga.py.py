import random

def parosDb(lista):
   return len([i for i in lista if i%2==0])




szamok=[random.randrange(10000,100000) for _ in range(500)]
    #print(szamok)


def paratlanOsszeg(lista):
   print("A páratlan számok összeg {}".format(sum([i for i in lista if i%2==1])))

   if sum(szamok[:len(szamok)/2]) > sum(szamok[len(szamok)/2:]):
      print("Az első fele nagyobb.")
    elif sum(szamok[:len(szamok)/2]) < sum(szamok[len(szamok)/2:]):
      print("A második fele nagyobb.")
    else: print("Egyenlőek")
   
db=len([i for i in szamok if i//10000==3])
db=len([i for i in szamok if str(i)[0]=="3"])
db=len([i for i in szamok if str(i).startswith("3")])
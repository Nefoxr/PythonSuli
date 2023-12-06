f=open("béla.txt", "w")

#f.write("1")
for i in range(100):
    f.write(str(i)+"\n")
f.close()


open("béla2.txt","w").write("\n".join([str.(i) for i in range(100)]))

f=open("béla.txt","r+")
lista=[]
for egySor in f:
    lista.append(egySor.strip())
f.close()
print(lista)

f=open("béla.txt","r")
lista=[f.readlines() for egySor in f.readlines()]

f.close()
print(lista)

result = map(lambda x: x.strip(), f.readlines())
print(list(lista2))
f.close()
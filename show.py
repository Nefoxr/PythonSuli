import random

maxWidth=80
maxHeight=25

minFlakes=0
maxFlakes=5

rows=[]
for _ in range(maxHeight):

actFlakes=ramdom.randint(minFlakes,maxFlakes)
actRow=" "*maxWidth

flakes=random.sample(range(0,maxWidth),actFlakes)
print(flakes)

for i in flakes:
    actRow=actRow[:i]+"*"+actRow[i+1:]

rows.append(actRow)

print(actRow)
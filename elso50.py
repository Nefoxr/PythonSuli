#Irassátok ki az 50 első nemnegatív számot!

for c in range(0,51):
    print(c)

#Irassátok ki a kétjegyű számokat!

for i in range(10,100):
    print(i)

#-''- 100-nál kisebb 7-tel osztható

for g in range(7,100,7):
    print(g)

# 500 és 2000 között, ahol a tizesek helyén 8 van!

for a in range(500,2001):
    tizes = a // 10 % 10
    if tizes == 8:
        print(a)

# Négyzetszámok amelyekn 3 jegyűek!

for ny in range(10,32):
    negyzet = ny ** 2
    if 100 <= negyzet <= 999:
        print(ny)

#Karacsonyfa

num = 3
for i in range(1, num+1):
	print(" "*(2*num-i+3), end="")
	for j in range(1, i+1):
		print("*", end=" ")
	print()

for i in range(1, num+3):
	print(" "*(2*num-i+1), end="")
	for j in range(-1, i+1):
		print("*", end=" ")
	print()

for i in range(1, num+5):
	print(" "*(2*num-i), end="")
	for j in range(-2, i+1):
		print("*", end=" ")
	print()

for i in range(1, num+3):
	print(" "*((2*num)), end="")
	print("* "*3)


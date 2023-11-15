import random

maganhangzok = ['a' 'e' 'i' 'o' 'u']  # magánhangzók
massalhangzok = ['b' 'c' 'd' 'f' 'g' 'h' 'j' 'k' 'l' 'm' 'n' 'p' 'q' 'r' 's' 't' 'v' 'w' 'x' 'y' 'z']  # mássalhangzók

szo = ''
for i in range(5):
    if i % 2 == 0:
        szo += random.choice(maganhangzok)
    else:
        szo += random.choice(massalhangzok)

print(szo)

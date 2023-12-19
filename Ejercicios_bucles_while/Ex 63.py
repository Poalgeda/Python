#Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número.

import random
tiros=0
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0
while tiros !=100:
    tiros +=1
    num=random.randint(1, 6)
    if num == 1:
        uno +=1
    elif num ==2:
        dos +=1
    elif num==3:
        tres+=1
    elif num==4:
        cuatro +=1
    elif num == 5:
        cinco +=1
    elif num == 6:
        seis +=1


print(f"Unos: {uno}")
print(f"Doses: {dos}")
print(f"Treses: {tres}")
print(f"Cuatros: {cuatro}")
print(f"Cincos: {cinco}")
print(f"Seises: {seis}")
#Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos. 
import time
import random
var1=time.perf_counter()
var2=0
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0
while var2 <3:
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
    var2=time.perf_counter()-var1

print(f"Unos: {uno}")
print(f"Doses: {dos}")
print(f"Treses: {tres}")
print(f"Cuatros: {cuatro}")
print(f"Cincos: {cinco}")
print(f"Seises: {seis}")


  

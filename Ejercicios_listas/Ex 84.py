#A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta.  El usuario tendrá 3 oportunidades para adivinar la palabra. 

import random

lista=['casa','barco','gato','perro','madera','agua','puente','pantalón']
var1=random.randint(0,len(lista)-1)
var2=[]
for y in lista[var1]:
    var2+=y.split(",")
random.shuffle(var2)
intentos=0
#esta variablñe es para no usar un break y salir del bucle.
while intentos !=3:
    print(var2)
    x=input("Introduce la palabra correcta: ")
    if x == lista[var1]:
        print("¡Acertaste!")
        #prové con mas variables.
        break
    elif x != lista[var1]:
        intentos+=1
        print(f"No has acertado, llevas {intentos} intento/s")

if intentos >=3:
    print("Te has quedado sin intentos. :(")
else:
    print("Fin del programa")
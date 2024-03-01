#Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así sucesivamente.

import random
lista=['casa','barco','gato','perro','madera','agua','puente','pantalón']
var1=random.randint(0,len(lista)-1)
var2=lista[var1]

acierto=True
#Con este while se pregunta constantemente el valor.
print(lista)
while acierto==True:
    var3=input("Introduce un valor de la lista: ")
    if var2==var3:
        acierto=False
        print("ACERTASTE")
    else:
        print("SIGUE JUGANDO")

print("Fin del programa")
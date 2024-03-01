#Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra 

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
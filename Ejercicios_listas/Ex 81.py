# A partir de una lista definida, busca el método apropiado para que se visualice un valor de la lista al azar.
import random
lista=['casa','barco','gato','perro','madera','agua','puente','pantalón']
var1=random.randint(0,len(lista)-1)
print(lista[var1])

#A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.

lista1=['casa','mesa','sal','sol','agua']
lista2=['casa','luz','tres','tren','sol','pan']
repetidos=[]
no_repetidos=[]
num1=len(lista2)
#Que vaya valor por valor comprovando si se repiten y se vayan sumando a sus correspondientes listas.
for cont in lista2:
    if lista2[0] == cont:
        repetidos += lista2[0].split(",")
    else:
        no_repetidos += lista2[0].split(",")
        lista2.pop(0)
#visualizar por pantalla.
print(repetidos)
print(no_repetidos)
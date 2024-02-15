#A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.
input()
lista1=['casa','mesa','sal','sol','agua']
lista2=['casa','luz','tres','tren','sol','pan']
repetidos=[]
no_repetidos=[]
#Que vaya valor por valor comprovando si se repiten y se vayan sumando a sus correspondientes listas.
for cont in lista1:
    if cont in lista2:
        repetidos += cont.split(",")
        i = lista2.index(cont)
        lista2.pop(i)
    else:
        no_repetidos += lista2[0].split(",")
        no_repetidos += cont.split(",")
        lista2.pop(0)
#visualizar por pantalla.
print(repetidos)
print(no_repetidos)
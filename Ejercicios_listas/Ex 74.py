#A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.

lista1=['casa','mesa','sal','sol','agua']
lista2=['casa','luz','tres','tren','sol','pan']
repetidos=[]
no_repetidos=[]
num1=len(lista2)
#Que vaya valor por valor comprovando si se repiten.
for cont in range(0, num1):
    if lista2[0] in lista1:
        i = lista1.index(lista2[0])
        
        repetidos += lista2[0].split(",")
        lista2.pop(0)
    else:
        no_repetidos += lista2[0].split(",")
        no_repetidos +=
        lista2.pop(0)
#visualizar por pantalla.
print(repetidos)
print(no_repetidos)
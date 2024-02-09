#Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2  (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no.

lista1=['casa','mesa','sal','sol','agua']
lista2=['casa','luz','tres','tren','sol','pan']
repetidos=[]
no_repetidos=[]
num1=len(lista2)
#Que vaya valor por valor comprovando si se repiten.
for cont in range(0, num1):
    if lista2[0] in lista1:
        repetidos += lista2[0].split(",")
        lista2.pop(0)
    else:
        no_repetidos += lista2[0].split(",")
        lista2.pop(0)
#visualizar por pantalla.
print(repetidos)
print(no_repetidos)
import random

lista_palabrasecreta=["ordenadores","habitación","mundos","tiempo","derechos","escuela","empresarios","gobierno","palabra","comunidad"]
lista_partida=[]
lista_ahorcado=[]
ahorcado=["A","H","O","R","C","A","D","O"]
intentos=0
palabra=list(random.choice(lista_palabrasecreta))

for cont in range (0, len(palabra)):
    lista_partida+="_".split(",")
print(lista_partida)
while intentos!=8 and lista_partida!=palabra:
    var=input("Introduce una letra: ")
    for x in palabra:
        if var==x:
            i=x.index(palabra)
            lista_partida[i]=var
            print("Enhorabuena, has acertado un letra.")
            print(lista_partida)
    if var not in palabra:
            intentos+=1
            print("Esta letra no existe en la palabra...")
            lista_ahorcado+=ahorcado[0].split(" ")
            ahorcado.pop(0)
            print(lista_ahorcado)
if intentos==8:
     print("Has perdido! Te has quedado sin intentos.")
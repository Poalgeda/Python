import random

lista_palabrasecreta=["ordenadores","habitación","mundos","tiempo","derechos","escuela","empresarios","gobierno","palabra","comunidad"]
lista_partida=[]
lista_ahorcado=[]
posicion=0
ahorcado=["A","H","O","R","C","A","D","O"]
palabra=list(random.choice(lista_palabrasecreta))

for cont in range (0, len(palabra)):
    lista_partida+="_".split(",")
while len(lista_ahorcado)==8 or lista_partida==palabra:
    var=input("Introduce una letra: ")
    for x in palabra:
        if var==x:
            lista_partida[posicion]=x
            posicion+=1
            print("Enhorabuena, has acertado un letra.")
            print(lista_partida)
    if var not in palabra:
        print("Esta letra no existe en la palabra...")
        lista_ahorcado+=ahorcado[0].split(" ")
        ahorcado.pop(0)



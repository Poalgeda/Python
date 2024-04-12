import random
import time
#mi lista vvv
lista_palabrasecreta=["ordenadores","habitación","mundos","tiempo","derechos","escuela","empresarios","gobierno","palabra","comunidad"]

respuesta="s"
lista_aciertos=[]
lista_errores=[]
while respuesta=="s":
    minutos=0
    lista_partida=[]
    lista_ahorcado=[]
    ahorcado=["A","H","O","R","C","A","D","O"]
    intentos=0
    barra=1
    #"random.choice" para que eliga una palabra random.
    palabra=list(random.choice(lista_palabrasecreta))
    for cont in range (0, len(palabra)):
        lista_partida+="_".split(",")
    print(lista_partida)
    start_time = time.time()
    while intentos!=8 and barra!=0:
        var=input("Introduce una letra: ")
        #primero miro si se falla la letra, luego que pasa si es correcta.
        if var not in palabra:
            intentos+=1
            print("Esta letra no existe en la palabra...")
            lista_ahorcado+=ahorcado[0].split(" ")
            ahorcado.pop(0)
            print(lista_ahorcado)
            lista_errores+=var
        for x in palabra:
            if var==x:
                i=palabra.index(x)
                lista_partida.pop(i)
                lista_partida.insert(i, var)
                e=palabra.count(var)
                if e>=2:
                    #si hay mas de una isma letra, para que el programa no se pete en vez de ir transportando letras, las clono y donde antes habia una dejo un guión.
                    palabra.pop(i)
                    palabra.insert(i, "-")
                lista_aciertos+=var
        print(lista_partida)
        print(f"Letras que no estan: {lista_errores}")
        barra=lista_partida.count("_")
    tiempo = time.time() - start_time
    tiempo= round(tiempo, 2)
    while tiempo>60:
        tiempo-=60
        minutos+=1
    if intentos==8:
         print("Has perdido! Te has quedado sin intentos.")
    else:
        print("Has Ganado! Has adivinado la palabra.")
        #print la info del final.
    print(f"Has tardado {minutos} minutos y {tiempo} segundos en terminar el programa.")
    if tiempo > 60:
        #Que se le notifique al jugador si ha tardado mas de un minuto en adivinar la palabra.
        print("Has tardado mas de un minuto :(")
    print(f"Has acertado {len(lista_aciertos)} letras")
    print(f"Has cometido {len(lista_errores)} errores ")
    respuesta=input("Quieres jugar otra partida? s/n ")
    #Si quiere añadir otra palabra lo pongo al final porque asi no se notifica al inicio de cada programa.
    #I depende de si solamente qui9ere hacer otra partida
    if respuesta=="s":
        q_añadir=input("Quieres añadir otra palabra la lista? s/n ")
        if q_añadir=="s":
            añadir=input("Introduce la palabra que quieres añadir a la lista inicial: ")
            lista_palabrasecreta+=añadir.split(",")

print("Fin del programa.")

#txt
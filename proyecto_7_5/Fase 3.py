#En esta fase tienes que conseguir que el usuario compita contra el ordenador (banca).
import time
import random
partida="s"
respuesta1="s"
respuesta2="s"
nickname=input("Introduce el nombre que quieres que salga por pantalla: ")
numeros=[1,2,3,4,5,6,7,10,11,12]
while partida == "s":
    total=0
    total2=0
    #---------------------------------turno del jugador--------------------------------------
    while respuesta1=="s":
        #Dandole valor al tipo de carta según en random.choice.
        carta=random.choice(numeros)
        if carta==1:
            num=1
        elif carta==2:
            num=2
        elif carta==3:
            num=3
        elif carta==4:
            num=4
        elif carta==5:
            num=5 
        elif carta==6:
            num=6
        elif carta==7:
            num=7
        elif carta==10:
            num=0.5
        elif carta==11:
            num=0.5
        elif carta==12:
            num=0.5
        total+=num
        #pedir de repetir la accion
        print("")
        print(f"Carta: {carta}. Total: {total}")
        if total <= 7:
            respuesta1=input("Quieres otra carta? s/n ")
        elif total ==7.5:
            respuesta1="n"
        elif total > 7.5:
            respuesta1 ="n"
    #---------------------------------turno de la banca--------------------------------------
    print("---------------------------------turno de la banca-------------------------------------------")
    print("                                                                                             ")
    print("                                                                                             ")
    while respuesta2=="s":
        #temporizador para que el jugador pueda seguir los movimientos de la banca.
        var1=time.perf_counter()
        var2=0
        while var2 <1.2:
            var2=time.perf_counter()-var1
        carta=random.choice(numeros)
        if carta==1:
            num=1
        elif carta==2:
            num=2
        elif carta==3:
            num=3
        elif carta==4:
            num=4
        elif carta==5:
            num=5 
        elif carta==6:
            num=6
        elif carta==7:
            num=7
        elif carta==10:
            num=0.5
        elif carta==11:
            num=0.5
        elif carta==12:
            num=0.5
        total2 +=num
        print(f"Carta: {carta}. Total: {total2}")
        var1=time.perf_counter()
        var2=0
        #Este codigo le da indicaciones a la banca según l9o que tenga el jugarj
        while var2 <2:
            var2=time.perf_counter()-var1
        if total2 <= 7:
            if total2 > total:
                print("-La banca se planta-")
                respuesta2="n"
            elif total > 7.5:
                if total2 <=4:
                    print("-La banca coge otra carta-")
                    respuesta2="s"
                else:
                    print("-La banca se planta-")
                    respuesta2="n"
            elif total <=7.5:
                if total2 <= 6:
                    print("-La banca coge otra carta-")
                    respuesta2="s"
        elif total2 ==7.5:
            print("-La banca se planta-")
            respuesta2="n"
        elif total2 > 7.5:
            print("-La banca se ha pasado-")
            respuesta2 ="n"
    #resultados.
    var2=0
    while var2 <1.5:
        var2=time.perf_counter()-var1
    if total==total2 and total <= 7.5 and total2 <= 7.5:
        print(f"Banca y {nickname} empatan.")
    elif total>total2 and total <= 7.5 and total2 <= 7.5:
        print(f"{nickname} gana la partida.")
    elif total<total2 and total <= 7.5 and total2 <= 7.5:
        print("La banca gana la partida")
    elif total > 7.5 and total2> 7.5:
        print(f"La banca y {nickname} pierden.")
    elif total>7.5 and total2 <=7.5:
        print("Gana la banca.")
    elif total2>7.5 and total <=7.5:
        print(f"Gana {nickname}.")

    partida=input("¿Quieres jugar otra partida? s/n ")
    if partida=="s":
        respuesta1="s"
        respuesta2="s"
#:)
print("Fin del programa 😊👍")
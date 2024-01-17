#En esta fase tienes que conseguir que el usuario compita contra el ordenador (banca).

import random
total=0
total2=0
respuesta1="s"
respuesta2="s"
nickname=input("Introduce el nombre que quieres que salga por pantalla: ")
numeros=[1,2,3,4,5,6,7,10,11,12]
#---------------------------------turno del jugador--------------------------------------
while respuesta1=="s":
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
    print("")
    print(f"Carta: {carta}. Total: {total}")
    if total <= 7:
        respuesta1=input("Quieres otra carta? s/n ")
    elif total ==7.5:
        respuesta1="n"
    elif total > 7.5:
        respuesta1 ="n"
#---------------------------------turno de la banca--------------------------------------
print("                                                                                             ")
print("                                                                                             ")
print("                                                                                             ")
while respuesta2=="s":
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
    if total2 <= 7:
        if total2 > total:
            print("-La banca se planta-")
            respuesta2="n"
        else:
            print("-La banca coge otra carta-")
            respuesta2="s"
                    
    elif total2 ==7.5:
        print("-La banca se planta-")
        respuesta2="n"
    elif total2 > 7.5:
        print("-La banca se ha pasado-")
        respuesta2 ="n"

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

print("Fin del programa 😊👍")
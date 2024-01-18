#Partes  de  un  depósito  de  100  puntos.  Dependiendo  del  resultado  de  una  partida,  tu  puntuación  severá aumentada o disminuida siguiendo los criterios (respeta los mensajes de la Fase 1)

import random
banca=100
total=0
respuesta1="s"
respuesta2="s"
numeros=[1,2,3,4,5,6,7,10,11,12]
while respuesta1=="s" and banca > 0:
    while respuesta2=="s" and banca > 0:
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
        print(f"Carta: {carta}. Total: {total}")
        if total <= 7:
            respuesta2=input("Quieres otra carta? s/n ")
        elif total ==7.5:
            respuesta2="n"
        elif total > 7.5:
            respuesta2 ="n"
    if total <6:  
        print("Quizás tendrías que arriesgar un poco ¿no?")
        banca -= 5
        print(f"¡Has perdido 5 puntos! Total: {banca}")
        print("--------------------------------------")
        respuesta1=input("Quieres jugar otra partida? s/n ")
    elif total >=6 and total <=7:
        print("Has sido un poco conservador")
        banca += 5
        print(f"¡Has ganado 5 puntos! Total: {banca}")
        print("--------------------------------------")
        respuesta1=input("Quieres jugar otra partida? s/n ")
    elif total > 7.5:
        print("Has perdido la ronda!")
        banca -= 10
        print(f"¡Has perdido 10 puntos! Total: {banca}")
        print("--------------------------------------")
        respuesta1=input("Quieres jugar otra partida? s/n ")
    elif total==7.5:
        print("Enhorabuena, has ganado la partida")
        banca += 10
        print(f"¡Has ganado 10 puntos! Total: {banca}")
        print("--------------------------------------")
        respuesta1=input("Quieres jugar otra partida? s/n ")
        print("--------------------------------------")
    total=0
    if respuesta1=="s":
        respuesta2 = "s"

if banca <= 0:
    print("Te has quedado sin puntos...😔")
else:
    print("Fin del programa. ╰(*°▽°*)╯")

#Programa  el  código  que  gestione  una  partida.  El  programa  ofrece  una  carta,  el  usuario  puede  o  noaceptar. La puntuación se acumula según el número de carta que aparece al azar.

import random
total=0
respuesta1="s"
respuesta2="s"
numeros=[1,2,3,4,5,6,7,10,11,12]
while respuesta1=="s":
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
        total+=num
        if total <= 7:
            respuesta2=input("Quieres otra carta? s/n")
        elif total ==7.5:
            respuesta2=="n"
        elif total > 7.5:
            .0
            respuesta2 =="n"
    if total >6:  
        print("Quizás tendrías que arriesgar un poco ¿no?")
    elif total <=6 and total >=7:
        print("Has sido un poco conservador")
    elif total > 7.5:
        print("Has perdido la partida!")
    elif total==7.5:
        print("Enhorabuena, has ganado la partida")
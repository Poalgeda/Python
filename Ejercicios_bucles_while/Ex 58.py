#Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random
num=random.randint(1, 5)
acierto= True
contador=0
while acierto == True and contador!=3:
    var1=int(input("Introduce un numero del uno al cinco: "))
    contador +=1
    if var1==num and var1 <=5 and var1 >0:
        acierto= False
        print("Numero acertado")
    elif var1!=num and var1 <=5 and var1 >0:
        print("Numero no acertado")
    else:
        print("Introduce un numero entre el 1 y el 5!!!")
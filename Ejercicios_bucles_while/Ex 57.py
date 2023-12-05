#Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5

import random
num=random.randint(1, 5)
acierto= True
while acierto == True:
    var1=int(input("Introduce un numero del uno al cinco: "))
    if var1==num and var1 <=5 and var1 >0:
        acierto= False
        print("Numero acertado")
    elif var1!=num and var1 <=5 and var1 >0:
        acierto = True
        print("Numero no acertado")
    else:
        print("Introduce un numero entre el 1 y el 5!!!")



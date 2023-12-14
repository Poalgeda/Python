#Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 

import random
num=random.randint(1, 1000)
acierto= True
intentos=0
while acierto == True:
    var1=int(input("Introduce un numero del uno al mil: "))
    intentos += 1
    if var1==num and var1 <=1000 and var1 >1:
        acierto= False
        print(f"Has acertado el numero {num}! Fin del programa.")
        print(f"Has realizado {intentos} intentos")
    elif var1!=num and var1 <=1000 and var1 >=1:
        acierto = True                                                      
        if var1 > num:
            print("El numero secreto es menor.")
        elif var1 < num:
            print("El numero secreto es mayor.")
        
    else:
        print("Introduce un numero entre el 1 y el 1000.")

        

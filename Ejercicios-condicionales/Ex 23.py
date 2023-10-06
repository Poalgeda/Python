#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.


nota=float(input("Introduce tu nota del 0 al 10: "))


if nota<=10:
    if nota>=0:
        if nota<5:
            print("Tu nota es:", nota, ", has sacado un insuficiente.")
        elif nota>=8.5:
            print("Tu nota es:", nota,",has sacado un excelente.")
        else:
            if nota<6.5:
                print("Tu nota es:", nota,", has sacado un satisfactorio.")
            else:
                print("Tu nota es:", nota,", has sacado un notable.")
            input()    
    else:
        print("El valor establecido no esta dentro de los limites establecidos")
        input()
else: 
    print("El valor establecido no esta dentro de los limites establecidos")
    input()

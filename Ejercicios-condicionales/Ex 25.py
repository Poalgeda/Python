#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

nota=float(input("Introduce tu nota del 0 al 10: "))

if nota<=10 and nota >=0:
    if nota<5:
        print("Tu nota es un",nota,"y has suspendido")
    elif nota>=5 and nota<6.5:
        print("Tu nota es un",nota,"y has sacado un satisfactorio")
    elif nota>=6.5 and nota<8.5:
        print("Tu nota es un",nota,"y has sacado un notable")
    else:
        print("Tu nota es un",nota,"y has sacado un excelente")
else:
    print("La nota introducida no esta entre 0 y 10")
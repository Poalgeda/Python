#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.


nota=float(input("Introduce tu nota del 0 al 10"))

if nota<5 and nota>0 and nota<10:
    print ("Has suspendido sacando un ", nota)
    input()
elif nota>5 or nota==5:
    print("Has aprovado sacando ", nota)
    input()
else:
    print("El valor establecido no esta dentro de los limites establecidos")
    input()

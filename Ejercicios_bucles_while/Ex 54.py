#Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural..       . Con While

repeticiones=0
suma_total=0

while suma_total <= 50:
    var1=int(input("Introduce el primer numero: "))
    var2=int(input("Introduce el segundo numero: "))
    suma=var1+var2
    suma_total+=suma
    repeticiones+=1
    print(f"El resultado de la suma es {suma}")
    if repeticiones == 1:
        print(f"El total acumulado es: {suma_total} y llevas {repeticiones} operación realizada.")
    else:
        print(f"El total acumulado es: {suma_total} y llevas {repeticiones} operaciones realizadas.")


print("Fin del programa")
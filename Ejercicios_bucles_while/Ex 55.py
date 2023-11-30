#Última vez que reutilizamos el mismo código.. lo prometo. A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

repeticiones=0
suma_total=0
resto=0


while suma_total <= 50 or resto == 0:
    var1=int(input("Introduce el primer numero: "))
    var2=int(input("Introduce el segundo numero: "))
    suma=var1+var2
    suma_total+=suma
    repeticiones+=1
    resto=suma_total % 2
    print(f"El resultado de la suma es {suma}")
    if repeticiones == 1:
        print(f"El total acumulado es: {suma_total} y llevas {repeticiones} operación realizada.")
    else:
        print(f"El total acumulado es: {suma_total} y llevas {repeticiones} operaciónes realizadas.")


print("Fin del programa")
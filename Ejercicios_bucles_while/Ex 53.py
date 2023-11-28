#A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While

repeticiones=0
suma_total=0
respuesta = "s"

while respuesta == "s":
    var1=int(input("Introduce el primer numero: "))
    var2=int(input("Introduce el primer numero: "))
    suma=var1+var2
    suma_total+=suma
    repeticiones+=1
    print(f"El resultado de la suma es {suma}")
    respuesta=input("¿Deseas repetir la operación? s/n: ")

print("Fin del programa")
print(f"La suma total es: {suma_total} y el numero de repeticiones es: {repeticiones}.")
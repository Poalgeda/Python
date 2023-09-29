# Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
var1=int(input("Introduce un numero:  "))
var2=int(input("Introduce otro numero:  "))

if var1>var2:
    print("El numero",var1,"es mayor que", var2,".")

elif var2>var1:
    print("El numero",var2,"es mayor que", var1,".")
else:
    print ("Ambos numeros", var1 ,"y", var2, "son iguales.")

input()
# A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10

var1=int(input("Introduce un numero entre 0 y 10:  "))
var2=int(input("Introduce otro numero entre 0 y 10:  "))

if var1>var2 and var1>0 and var1<10 and var2>0 and var2<10:
    print("El numero",var1,"es mayor que", var2,".")

elif var2>var1 and var1>0 and var1<10 and var2>0 and var2<10:
    print("El numero",var2,"es mayor que", var1,".")
elif var1==var2 and var1>0 and var1<10 and var2>0 and var2<10:
    print ("Ambos numeros", var1 ,"y", var2, "son iguales.")

else:
    print("Uno o los dos numeros estan fuera del límite establecido")

input()

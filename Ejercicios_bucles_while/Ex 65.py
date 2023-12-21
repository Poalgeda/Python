#Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.




var1=0
var1=int(input("Introduce un numero: "))
num_mayor=var1
num_menor=var1
while var1 != -99:
    if var1 > num_mayor:
        num_mayor=var1
    elif var1 < num_menor:
        num_menor=var1
    var1=int(input("Introduce un numero: "))

print("*****RESUMEN*****")

print(f"Numero más grande: {num_mayor}")
print(f"Numero más pequeño: {num_menor}")
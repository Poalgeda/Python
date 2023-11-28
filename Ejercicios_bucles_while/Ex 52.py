#Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While 

respuesta = "s"
while respuesta == "s":
    var1=int(input("Introduce el primer numero: "))
    var2=int(input("Introduce el primer numero: "))
    suma=var1+var2
    print(f"El resultado de la suma es {suma}")
    respuesta=input("¿Deseas repetir la operación? s/n: ")

input("Fin del programa")
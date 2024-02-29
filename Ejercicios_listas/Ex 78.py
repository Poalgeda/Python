#A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
 
lista=['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']
respuesta="s"
print(lista)
while respuesta=="s":
    #var1 es el valor que se desea eliminar.
    var1=input("Introduce el valor que deseas eliminar: ")
    if var1 not in lista:
        print("El valor introducido no esta en la lista")
#He puesto un .lower y un .isupper porque con otros metodos me detectaba que los numeros tambien contaban.
    elif var1.islower() or var1.isupper():
        print("Introduce un valor numérico: ")
    elif var1.isnumeric():
        lista.remove(str(var1))
        print(lista)
    respuesta=input("Desea Introducir otro valor? s/n ")

print("fin del programa")
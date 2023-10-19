# Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

var1=input("Introduce una letra:  ")

numero=var1.isdigit()
caracter=var1.isascii()
if numero is True:
    print("El valor introducido es un numero.")
elif numero is False and caracter is False:
    if 'A' <= var1 <= 'Z': 
            mayuscula = True
    else:
            mayuscula = False
    if mayuscula:
            print("La letra ingresada está en mayúscula.") 
    else:
            print("La letra ingresada está en minúscula.")
elif caracter is True:
    print("El valor introducido no es ni un numero ni una letra.")
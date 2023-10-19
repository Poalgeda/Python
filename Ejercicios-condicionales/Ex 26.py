#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.


letra = input("Por favor, ingrese una letra: ")
mayuscula=letra.isupper()

if 'A' <= letra <= 'Z': 
    mayuscula = True
else:
    mayuscula = False

if mayuscula:
    print("La letra ingresada está en mayúscula.")
else:
    print("La letra ingresada no está en mayúscula.")
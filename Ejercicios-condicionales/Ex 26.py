#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
import string

var1=input(str("Introduce una letra, mayúscula o minúscula:  "))

if var1==string.ascii_lowercase:
    print("Minúscula")
else:
    print("Mayúscula")
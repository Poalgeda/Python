#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.


var1=input("Introduce una letra, mayúscula o minúscula:  ")

mayuscula=var1.isupper()

if mayuscula is True:
    print("Es mayuscula")
elif mayuscula is False:
    print("Es minuscula")
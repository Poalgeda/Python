#Realiza un programa que controle si la longitud de una frase introducida por teclado es
#igual, menor o mayor de 11 caracteres. Utiliza elif.
var1=input("introduce una frase: ")
leng=len(var1)
if leng>11:
    print("la frase tiene mas de 11 caracteres")
elif leng<11:
    print("la frase tiene menos de 11 caracteres")
else:
    print("la frase tiene 11 caracteres")
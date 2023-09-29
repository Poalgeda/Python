#Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.

var1=int(input("Introduce el primer numero"))
var2=int(input("Introduce el segundo numero"))
total=var1//var2
resto=var1 % var2

    
print("El cociente es: ", float(total))
print("El resto es: ",resto)
if resto==0: print("El dividendo es par")
else: print("El dividendo es impar")
input()

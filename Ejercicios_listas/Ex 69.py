#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.


total=""
num=int(input("Cuantos numeros quieres introducir: "))
for cont in range(0,num):
    var1=input("Introduce un numero:")
    total+=var1
    lista=total.split(",")
    lista=total.sort()
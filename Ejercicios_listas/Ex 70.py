#Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo. 

lista=[]
lista2=[]
num=int(input("Cuantas palabras quieres introducir: "))
for cont in range(0,num):
    var1 =input("Introduce una palabra: ")
    lista += sorted(var1.split(","))
    lista2 += var1.split(",")
lista.sort(reverse=False)
print(lista)
lista2.sort(reverse=True)
print(lista2)

#Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas: 
#a) total de pares 
#b) total de impares 
#c) total de números positivos 
#d) total de números negativos 
#e) total de ceros 
#f) total de la suma de todos los números introducidos

ceros=0
pares=0
impares=0
positivos=0
negativos=0
Suma=0

while var1 != -99:
    var1=int(input("Introduce un numero: "))
    if var1 == 0:
        ceros +=1
    resto= % 2
    if resto==0 and var1!=0:
        pares+=1
    else:
        impares =+1
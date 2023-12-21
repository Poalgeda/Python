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
var1=0
var1=int(input("Introduce un numero: "))
while var1 != -99:
    resto= var1 % 2
    if var1 == 0:
        ceros +=1
    elif resto==0:
        pares+=1
    elif resto > 0 or resto < 0:
        impares =+1
    if var1 > 0:
        positivos +=1
    elif var1 < 0:
        negativos +=1
    Suma +=var1
    var1=int(input("Introduce un numero: "))

print("*****RESUMEN*****")
print(f"Ceros: {ceros}")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")
print(f"Suma total: {Suma}")
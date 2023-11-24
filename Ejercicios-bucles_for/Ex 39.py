#Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.

var1=int(input("Cuantos numeros quieres introducir?"))
var_ceros=0
var_positivos=0
var_negativos=0

for cont in range(0, var1):
    num=float(input("Introduce un numero: "))
    if num >0:
        var_positivos+=1
    elif num <0:        
        var_negativos+=1
    elif num == 0:
        var_ceros +=1


print("Positivos: ", var_positivos)
print("Negativos: ",var_negativos)
print("Ceros: ",var_ceros)

input()
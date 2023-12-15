#Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo. 

var1=int(input("Introduce el numero inferior: "))
var2=int(input("Introduce el numero superior: "))
output1=""
output2=""
for cont in range(var1,var2,):
    resto=cont % 2
    if resto==0:
        output1 += str(cont)
        output1 +="-"
    else:
        output2 += str(cont)
        output2 +="-"

output1=output1[:-1]
output2=output2[:-1]

print(f"Los numeros pares son: {output1}")
print(f"Los numeros impares son: {output2}")

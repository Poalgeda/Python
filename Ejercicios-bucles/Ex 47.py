# Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida

var1=int(input("Introduce el primer intervalo: "))
var2=int(input("Introduce el segundo intervalo: "))

num_1=""
num_2=""

if var1>var2:
    rango=var1-var2+1
else:
    rango=var2-var1+1

for cont in range(0, rango):
    
    num_1 + "{cont}" + "-"

print(num_1)
#Ejercicio 3
import math
lado=float(input("Introduce el valor de lado del triangulo: "))
area=(math.sqrt(3)/4) * (lado**2)
area_total=round(area,2)
print("El area del triangulo equilatero es: ",area_total)
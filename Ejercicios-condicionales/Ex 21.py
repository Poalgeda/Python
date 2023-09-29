# Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo.
import math
a=int(input("Introduce el numero que tiene la incognita elevada al cuadrado:  "))
b=int(input("Introduce el numero que tiene una incognita :  "))
c=int(input("Introduce el numero independiente:  "))
raiz=math.sqrt(b**2-4*a*c)

if raiz<0:
    print("Como la raiz es negativa no tiene un resultado posible")
elif raiz>0:
    x1=(-b+raiz)/(2*a)
x2= (-b-raiz)/(2*a)
print("La raiz es positiva: x1=",float(x1)," x2=", float(x2),".")

elif raiz==0: 
x= -b/(2*a)
print("Como la raiz es igual a 0, solo hay un resultado posible, x=", float(x))
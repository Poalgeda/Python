#Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

import math
pi=math.pi
r=int(input("Introduce el radio de la base del cilindro:  "))
h=int(input("Introduce la altura del cilindro:  "))
d=r*2
ab=r**2*pi
ar=d*pi*h
at=ab*2+ar
v=ab*h
vred= round( v , 2)
atred= round( at , 2)
print("El area del cilindro es:  ", atred)
print("El volumen del cilindro es:", vred)
input()
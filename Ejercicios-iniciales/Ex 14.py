# Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math
diam=int(input("Introduce el diametro del circulo: "))
r=diam/2
pi= math.pi
p=2*pi*r
a=r**2*pi
pr= round ( p , 1)
ar= round ( a , 1)
print("El perímetro del circulo es:  ", pr)
print("El area del circulo es:  ", ar)
input()

# Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).
import math
var1=int(input("Introduce un valor: "))
raiz=math.sqrt(var1)
div= raiz//2
r=round( raiz , 1)
d= round ( div , 1)
print("El resultado de la raíz es: ", float(r))
print("El resultado de la división: ", float(d))
input()

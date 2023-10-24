#Corrige los 4 errores o añade el código que necesites para que el siguiente programa se 
#ejecute correctamente
#inicializo valores a cada variable
var_num="6734"
var_suma=0
#obtengo su longitud
var_long=len(var_num)
#sumo cada digito a partir del índice de cada posición
var_suma = int(var_num[0]) + int(var_num[1])+ int(var_num[2]) + int(var_num[3])
#utilizo una condición y el operador aritmético // para saber si el resto da 0 y ver si es par
if var_suma % 2 == 0:
    print (f"el valor de {var_suma} es par")
else:
    print(f"el valor de {var_suma} es impar")
#Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por pantalla los siguientes resultados: 
#a. Cantidad total de valores 
#b. Cantidad de números 
#c. Cantidad de letras 
#d. Cantidad de mayúsculas 
#e. Suma de los valores numéricos

lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']

total = len(lista1)
numeros = 0
mayusculas = 0
letras=0
suma_nums = 0
for elemento in lista1:
    if elemento.isdigit():
        numeros += 1
    if elemento.isalpha():
        letras += 1
    if elemento.isdigit():
        suma_nums += int(elemento)
    if elemento.isupper():
        mayusculas += 1

print("Número de valores:", total)
print("Cantidad de números:", numeros)
print("Cantidad de letras:", letras)
print("Cantidad de mayúsculas:", mayusculas)
print("Suma total de números:", suma_nums)
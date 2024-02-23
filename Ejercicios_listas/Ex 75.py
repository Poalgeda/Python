#Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por pantalla los siguientes resultados: 
#a. Cantidad total de valores 
#b. Cantidad de números 
#c. Cantidad de letras 
#d. Cantidad de mayúsculas 
#e. Suma de los valores numéricos

#valores :)
lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']

valores = len(lista1)
numeros = 0
mayusculas = 0
letras=0
suma_nums = 0
#que detecte el programa que tipo de caracteres son y vaya haciendo las operaciones necesarias.
for elemento in lista1:
    if elemento.isdigit():
        numeros += 1
    if elemento.isalpha():
        letras += 1
    if elemento.isdigit():
        suma_nums += int(elemento)
    if elemento.isupper():
        mayusculas += 1

#print lo que se pide.
print(f"Número de valores: {valores}")
print(f"Cantidad de números: {numeros}")
print(f"Cantidad de letras: {letras}")
print(f"Cantidad de mayúsculas: {mayusculas}")
print(f"Suma total de números: {suma_nums}")
#A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo. 


#definicion de valores.
lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']
valores = len(lista1)
mayusculas = []
lista_numeros=[]
lista_letras=[]
var1="a"

#Que adjudique una lista por si es numero o letra, las mayusculas tambien las añado en una lista aparte para detectar cuales son 
#Y mas tarde insertarlas, con ayuda de un for, en la posicion que les toca.
for elemento in lista1:
    if elemento.isdigit():
        lista_numeros+=elemento.split(",")
    if elemento.isalpha() and elemento.islower():
        lista_letras+=elemento.split(",")
    if elemento.isupper() and elemento.isalpha():
        mayusculas += elemento.split(",")
#He añadido un while para que se tenga que poner un 1 o un 2 y si no se cumple el programa te avisa, en vez de que salga un error en la consola.
while var1=="a":
    asc_desc=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: "))
    if asc_desc !=1 and asc_desc !=2:
        print("Por favor, introduce el número 1 o 2.")
        var1="a"
    elif asc_desc == 1:
        lista_numeros.sort()
        lista_letras.sort()
        for 
        #Como habrán ahora dos letras repetidas con el nombre de 'x', elegimos la segunda y la convertimos en mayuscula, reciclando variables.
        
        print(lista_numeros)
        print(lista_letras)
        
    elif asc_desc == 2:
        lista_numeros.sort(reverse=True)
        lista_letras.sort(reverse=True)
        print(lista_numeros)
        print(lista_letras)
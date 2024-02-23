#A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo. 


#definicion de valores.
lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']
valores = len(lista1)
mayusculas = []
lista_numeros=[]
lista_letras=[]
var1="a"

#Que adjudique una lista por si es numero o letra, las mayusculas tambien els añado en una lista aparte para detectar cuales son 
#Y mas tarde convertirlas en minusculas, para ordenar la lista y luego convertirlas nuevamente en mayúsculas.
for elemento in lista1:
    if elemento.isdigit():
        lista_numeros+=elemento.split(",")
    if elemento.isalpha():
        lista_letras+=elemento.split(",")
    if elemento.isupper():
        mayusculas += elemento.split(",")

#He añadido un while para que se tenga que poner un 1 o un 2 y si no se cumple el programa te avisa, en vez de que salga un error en la consola.
while var1=="a":
    asc_desc=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: "))
    if asc_desc !=1 and asc_desc !=2:
        print("Por favor, introduce el número 1 o 2.")
        var1="a"
    elif asc_desc == 1:
        #localizar las mayusculas
        i_1=lista_letras.index("X")
        i_2=lista_letras.index("D")
        i_1=str(i_1).lower()
        i_2=str(i_2).lower()
        lista_numeros.sort()
        lista_letras.sort()
        
        print(lista_numeros)
        print(lista_letras)
    elif asc_desc == 2:
        lista_numeros.sort(reverse=True)
        lista_letras.sort(reverse=True)
        print(lista_numeros)
        print(lista_letras)
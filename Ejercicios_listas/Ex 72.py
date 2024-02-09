#A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista 

respuesta="s"
lista=[]
vocal=None


while respuesta=="s":
    #Convierte una vocal con tilde a una normal.
    letra=input("Introduce una letra: ")
    letra = letra.lower()
    if letra in "aáàäâ":
        letra="a"
    elif letra in "eéèëê":
        letra="e"
    elif letra in "iíìïî":
        letra="i"
    elif letra in "oóòöô":
        letra="o"
    elif letra in "uúùüû":
        letra="u"
    #Controla si la vocal esta o no en la lista y si es valida.
    if letra in lista:
        respuesta=input("Quieres repetir? s/n ")
    elif letra in "abcçdefghijklmnñopqrstuvwxyz":
        lista+=letra.split(",")
        respuesta=input("Quieres repetir? s/n ")
    else:
        None
print(lista)
#A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista 

respuesta="s"
lista=[]
vocal=None
def vocales():
    if letra in "aáàä":
        letra="a"
        vocal=True
    elif letra in "eéèë":
        letra="e"
        vocal=True
    elif letra in "iíìï":
        letra="i"
        vocal=True
    elif letra in "oóòö":
        letra="o"
        vocal=True
    elif letra in "uúùü":
        letra="u"
        vocal=True
    else:
        vocal=False


while respuesta=="s":
    #Controlador de letras.
    letra=input("Introduce una letra: ")
    letra = letra.lower()
    letra = vocales(letra)
    if vocal==True:
        
        
    if letra in lista:
        respuesta=input("Quieres repetir? s/n ")
    elif letra in "abcçdefghijklmnñopqrstuvwxyz":
        lista+=letra.split(",")
        respuesta=input("Quieres repetir? s/n ")
    else:
        None


print(lista)
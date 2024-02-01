#Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas. 

respuesta="s"
lista=[]
while respuesta=="s":
    letra=input("Introduce una letra: ")
    if letra in lista:
        print()
        respuesta=input("Quieres repetir? s/n ")
    elif letra.isa:
        lista+=letra.split(",")
        respuesta=input("Quieres repetir? s/n ")
    else:
        print()

print(lista)
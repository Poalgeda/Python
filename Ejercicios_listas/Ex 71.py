#Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas. 

respuesta="s"
lista=[]
while respuesta=="s":
    #Controlador de letras.
    letra=input("Introduce una letra: ")
    if letra in lista:
        respuesta=input("Quieres repetir? s/n ")
    elif letra in "áàabcçdèéefghíìijklmnñóòopqrstúùuvwxyzÁÀABCÇDÉÈEFGHÍÌJKLMNÑÒÓPQRSTÙÚVWXYZ":
        lista+=letra.split(",")
        respuesta=input("Quieres repetir? s/n ")
    else:
        None

print(lista)
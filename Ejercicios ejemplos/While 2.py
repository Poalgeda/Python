#Programa que con la introduccion de una nota te diga si esta suspendida o aprobada, y en caso de introducir una nota erronea te obligue a volver a introducir, esta funcion con un While.


respuesta=""
respuesta=input("¿Deseas empezar el programa? s/n ")


while respuesta == "s":
    nota=input("Introduce una nota: ")
    while nota.isalpha() or  int(nota)<0 or int(nota)>10:
        nota=input("Error, introduce de nuevo una nota: ")
    else:
        nota=int(nota)
        if nota >=5:
            print("aprobado")
        if nota < 5:
            print("suspendido")
    respuesta=input("¿Deseas continuar el programa? s/n ")


input("fin del programa")
#A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10.


var1=int(input("¿Cuantas notas quieres introducir? ----->"))

for cont in range (0, var1):
    nota=float(input("Introduce una nota: "))
    if nota >= 5 and nota <= 10:
        print("Esta aprovada :)")
    elif nota >= 0 and nota<5:
        print("Has suspendido")
    else:
        print("El valor numerico introducido esta fuera de los limites.")
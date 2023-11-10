# Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

var1=int(input("¿Cuantas notas quieres introducir? ----->"))

for cont in range (0, var1):
    nota=float(input("Introduce una nota: "))
    if nota >= 5:
        print("Esta aprovada :)")
    elif nota < 5:
        print("Has suspendido")



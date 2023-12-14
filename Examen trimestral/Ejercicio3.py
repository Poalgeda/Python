resultado=0
cifras=int(input("Cuantas cifras tiene el numero que quieres introducir? "))
num=int(input("Introduce el numero: "))
if cifras == len(str(num)):
    for var_recorrer in str(num):
        resultado += int(var_recorrer)
else:
    print("Error, no coincide el numero de cifras.")

if cifras == len(str(num)):
    print(f"Resultado: {resultado}")
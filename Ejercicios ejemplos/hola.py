# Inicializa el contador de errores
errores = 0

# Inicia un bucle para ingresar 5 números en escala
for i in range(5):
    try:
        numero = float(input(f'Ingresa el número en la posición {i + 1}: '))
        if numero < 0 or numero > 10:
            print("Error: El número debe estar en el rango de 0 a 10.")
            errores += 1
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        errores += 1

# Muestra el resultado
if errores == 0:
    print("Todos los números son válidos.")
else:
    print(f"{errores} error(es) en la entrada.")

#Programa que sume los n primeros números naturales. n Lo introduce el usuario.
num_nat = int(input("Introduce un número entero n: "))
suma = 0
for result in range(1, num_nat + 1):
    suma += result
print("La suma total de números naturales es:", suma)
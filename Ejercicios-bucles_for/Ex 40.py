#Crea un programa que cuente todos los números pares hasta el número 50.

num_pares=0
num_impares=0

for cont in range(0, 50):
    if cont % 2 == 0:
        num_pares+=1
    else:
        num_impares+=1

print(f"Hay {num_pares} numeros pares.")
print(f"Hay {num_impares} numeros impares.")
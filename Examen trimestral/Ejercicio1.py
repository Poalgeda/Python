
pos=0
neg=0
for cont in range(0,5):
    num=int(input("Introduce un numero: "))
    if num >= 0:
        pos +=1
    else:
        neg += 1

print(f"Suma de numeros positivos: {pos}")
print(f"Suma de numeros negativos: {neg}")
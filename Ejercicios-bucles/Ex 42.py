# Imprima el siguiente patrón con el ciclo for.


var1="*"

for cont in range(0, 4):
    print(var1)
    var1+="*"

for cont in range(0, 5):
    print(var1)
    var1=var1[1:]

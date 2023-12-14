var_min=int(input("Introduce el extremo mínimo del intervalo: "))
var_max=int(input("Introduce el extremo máximo del intervalo: "))
var_intervalo=int(input("Introduce la separación de los numeros en el intervalo: "))
output=""
for cont in range (var_min, var_max+1, var_intervalo):
    output += str(cont)
    output += ","
output=output[:-1]
    
print(output)
num=1 
var_total=50
while var_total <= 60 and num != 0:
    num=int(input("Introduce un numero: "))
    resto = num % 2
    if resto == 0:
        var_total += num
    else:
        var_total -= num
    print(var_total)
    

print("Fin del programa.")